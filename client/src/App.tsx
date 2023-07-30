import { useEffect, useState } from "react";
import "./App.css";
import { BarLoader } from "react-spinners";
import { Box, Modal } from "@mui/material";

const baseURL = `https://lagom-ilcjo546ka-ue.a.run.app`;
//const baseURL = `http://127.0.0.1:5000`;

interface Guess {
  guess: string;
  score: number;
  isWinner: boolean;
}
function App() {
  const initialGuess = {
    guess: "",
    score: -Infinity,
    isWinner: false,
  };
  const [err, setError] = useState<string>("");
  const [guessResponse, setGuessResponse] = useState<Guess[]>([]);
  const [win, setWin] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [riddle, setRiddle] = useState<string>("");
  const [attempt, setAttempt] = useState<number>(1);
  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const [bestGuess, setBestGuess] = useState<Guess>(initialGuess);

  const day = new Date();

  const style = {
    position: "absolute" as "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 350,
    bgcolor: "#000",
    border: "2px solid #fff",
    borderRadius: "20px",
    boxShadow: 24,
    p: 4,
  };

  useEffect(() => {
    setLoading(true);
    setError("");
    handleOpen();
    fetch(`${baseURL}/riddle`)
      .then((res) => {
        if (res.status !== 200) {
          setError("Unable to fetch riddle. Is the world ending?");
        } else {
          setError("");
          res.json().then((data) => {
            setRiddle(data.riddle);
          });
        }
      })
      .finally(() => setLoading(false));
  }, []);

  const handleFetch = (word: string) => {
    setLoading(true);
    fetch(`${baseURL}/game/${word}`)
      .then((res) => {
        if (res.status !== 200) {
          res.text().then((message) => setError(message));
        } else {
          setError("");
          res.json().then((data) => {
            if (data.isWinner) {
              setWin(true);
            }
            if (data.score > bestGuess.score) {
              setBestGuess(data);
            }

            setGuessResponse([data, ...guessResponse]);
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

  const handleLoss = () => {
    setLoading(true);
    fetch(`${baseURL}/giveup`)
      .then((res) => {
        if (res.status !== 200) {
          res.text().then((message) => setError(message));
        } else {
          setError("");
          res.json().then((data) => {
            setWin(true);
            setBestGuess(data);
            setGuessResponse([data, ...guessResponse]);
          });
        }
      })
      .finally(() => setLoading(false));
  };

  const handleHint = () => {
    if (attempt <= 3) {
      console.log("here");
      setLoading(true);
      fetch(`${baseURL}/hint/${attempt}`)
        .then((res) => {
          if (res.status !== 200) {
            res.text().then((message) => setError(message));
          } else {
            setError("");
            res.json().then((data) => {
              if (data.isWinner) {
                setWin(true);
              }
              if (data.score > bestGuess.score) {
                setBestGuess(data);
              }
              setGuessResponse([data, ...guessResponse]);
            });
          }
        })
        .finally(() => {
          setLoading(false);
          setAttempt(attempt + 1);
        });
    } else {
      setError("All hints used");
      return;
    }
  };

  return (
    <>
      <Modal
        open={!open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <div onClick={() => handleClose()} className="cursor-pointer">
            <p className="text-right">X</p>
          </div>
          <h2 className="mb-2 underline"> What's New?</h2>
          <ul className="mb-2 list-disc p-5">
            <li>Best guess is held at the top</li>
            <li>Loader bar for riddle</li>
            <li>Feel free to buy me a coffee!</li>
          </ul>
          <p>More features coming soon!</p>
        </Box>
      </Modal>

      <div className="m-auto">
        <h1 className="text-center m-10 font-bold underline">lagom</h1>
      </div>
      <div className="w-3/4 md:w-1/2 lg:w-1/3 xl:w-1/4 m-auto">
        <div className="grid gap-2 text-center grid-cols-3">
          <button
            onClick={() => {
              setBestGuess(initialGuess);
              setGuessResponse([]);
              setWin(false);
            }}
            className="text-center mb-5 font-bold  text-xs"
          >
            {win ? "You Win! Play again?" : "Reset"}
          </button>
          <button
            className="text-center mb-5 font-bold text-xs"
            onClick={() => handleLoss()}
          >
            Give up
          </button>

          <button
            className="text-center mb-5 font-bold text-xs"
            onClick={() => handleHint()}
          >
            Hint
          </button>
        </div>
      </div>

      <div className="m-auto w-3/4 md:w-1/2 lg:w-1/3 xl:w-1/4">
        <input
          className="w-full p-3 h-10 rounded-md"
          enterKeyHint="go"
          placeholder="Guess Here"
          onKeyPress={(e) => {
            handleEnter(e);
          }}
          disabled={win}
        ></input>
        <div className="text-center mt-5 mb-2">
          {loading ? (
            <BarLoader height={"0.5rem"} width={"100%"} color={"#ea738d"} />
          ) : (
            <div className="h-2"></div>
          )}
        </div>

        {riddle ? (
          <div>
            <h2
              className="underline mb-2"
              style={{ fontFamily: "Germania One, cursive" }}
            >
              {day.toLocaleDateString()}
            </h2>
            <div className="p-3">
              {riddle.split("\\n").map((i, key) => {
                return (
                  <p className="riddle" key={key}>
                    {i}
                  </p>
                );
              })}
            </div>
          </div>
        ) : (
          <></>
        )}

        <div className="m-5"> {err ?? <p>${err}</p>}</div>
        {bestGuess.guess ? (
          <div className="border-solid border-2 rounded-lg p-1 xl:w-full lg:w-full md:w-full sm:w-full w-10/12">
            <GuessCard
              guess={bestGuess.guess}
              score={bestGuess.score}
              isWinner={bestGuess.isWinner}
            />
          </div>
        ) : (
          <></>
        )}

        <div className="mt-5 mx-auto">
          {guessResponse.length == 0 ? (
            <>
              <h2 className="underline">How to play:</h2>
              <ol className="p-5 list-decimal">
                <li>
                  The answer to the riddle is always <u>one word</u>
                </li>
                <li>Your best guess will be highlighted at the top</li>
                <li>
                  Riddles can range from being obvious to tricky. Nothing is off
                  the table!
                </li>
                <li>Enter a word and see how close you are</li>
                <li>Scores will range from 0 - 100</li>
                <li>The higher the score the closer you are</li>
                <li>Click reset to clear guesses</li>
                <li>Click give up if you can't get it</li>
              </ol>
            </>
          ) : (
            guessResponse.map((guess, idx) => (
              <div
                key={idx}
                className="mb-1 xl:w-full lg:w-full md:w-full sm:w-full w-10/12 text-center"
              >
                <GuessCard
                  guess={guess.guess}
                  score={guess.score}
                  isWinner={guess.isWinner}
                />
              </div>
            ))
          )}
        </div>
      </div>
    </>
  );
}

const colors = ["#ff477e", "#5FA777"];

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

  let ratio = score / 100;
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
      className="flex justify-between p-3 border rounded-md border-black"
    >
      <p style={{ color: "black" }}>{guess}</p>
      <p style={{ color: "black" }}>{score}</p>
    </div>
  );
};
export default App;
