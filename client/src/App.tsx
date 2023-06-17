import { useState } from "react";
import "./App.css";
import { BarLoader } from "react-spinners";

const baseURL = `https://lagom-ilcjo546ka-ue.a.run.app`;
interface Guess {
  guess: string;
  score: number;
  isWinner: boolean;
}
function App() {
  const [err, setError] = useState<string>("");
  const [guessResponse, setGuessResponse] = useState<Guess[]>([]);
  const [win, setWin] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);

  const handleFetch = (word: string) => {
    setLoading(true);
    fetch(`${baseURL}/guess/1/${word}`)
      .then((res) => {
        if (res.status !== 200) {
          res.text().then((message) => setError(message));
        } else {
          setError("");
          res.json().then((data) => {
            if (data.isWinner) {
              setWin(true);
            }
            setGuessResponse([...guessResponse, data]);
          });
        }
      })
      .finally(() => setLoading(false));
  };

  const handleEnter = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      const word = (e.target as HTMLInputElement).value;
      (e.target as HTMLInputElement).value = "";
      handleFetch(word);
    }
  };

  return (
    <>
      <div className="m-auto">
        <h1 className="text-center m-10 font-bold underline">Lagom</h1>
      </div>
      <div className="text-center">
        <button
          onClick={() => {
            setGuessResponse([]);
            setWin(false);
          }}
          className="text-center mb-5 font-bold underline"
        >
          {win ? "You Win! Play again?" : "Reset"}
        </button>
      </div>
      <div className="m-auto w-3/4 md:w-1/2 lg:w-1/3 xl:w-1/4">
        <input
          className="w-full p-3 h-10 rounded-md"
          placeholder="Guess Here"
          onKeyPress={(e) => {
            handleEnter(e);
          }}
          disabled={win}
        ></input>
        <div className="text-center m-5 ">
          {loading ? (
            <BarLoader height={"0.5rem"} width={"100%"} color={"#ea738d"} />
          ) : (
            <div className="h-2"></div>
          )}
        </div>
        <div className="m-5"> {err ?? <p>${err}</p>}</div>

        <div className="mt-5 mx-auto">
          {guessResponse.length == 0 ? (
            <>
              <h2 className="underline">How to play:</h2>
              <ol className="p-5 list-decimal">
                <li>Enter a word and see how close you are</li>
                <li>A Number will represent how close you are</li>
                <li>Scores will range from 0-1</li>
                <li>Greener = Better</li>
                <li>Click reset to clear guesses</li>
              </ol>
            </>
          ) : (
            guessResponse.map((guess) => (
              <GuessCard
                guess={guess.guess}
                score={guess.score}
                isWinner={guess.isWinner}
              />
            ))
          )}
        </div>
      </div>
    </>
  );
}

const colors = ["#ff477e", "#6b9080"];

const GuessCard = ({ guess, score }: Guess) => {
  const interpolate = (start: number[], end: number[], ratio: number) => {
    const r = Math.trunc(ratio * end[0] + (1 - ratio) * start[0]);
    const g = Math.trunc(ratio * end[1] + (1 - ratio) * start[1]);
    const b = Math.trunc(ratio * end[2] + (1 - ratio) * start[2]);
    return [r, g, b];
  };

  const hexToRgb = (hex: string) => [
    parseInt(hex.substr(1, 2), 16),
    parseInt(hex.substr(3, 2), 16),
    parseInt(hex.substr(5, 2), 16),
  ];

  const rgbToHex = (rgb: number[]) =>
    "#" +
    rgb
      .map((x) => {
        const hex = x.toString(16);
        return hex.length === 1 ? "0" + hex : hex;
      })
      .join("");

  let ratio = score;
  if (score < 0) {
    ratio = 0;
  }
  const rgbInterpolated = interpolate(
    hexToRgb(colors[0]),
    hexToRgb(colors[1]),
    ratio
  );

  const color = rgbToHex(rgbInterpolated);
  return (
    <div
      style={{ backgroundColor: `${color}` }}
      className="flex justify-between p-3 mb-2 border rounded-md border-black"
    >
      <p style={{ color: "black" }}>{guess}</p>
      <p style={{ color: "black" }}>{score}</p>
    </div>
  );
};
export default App;
