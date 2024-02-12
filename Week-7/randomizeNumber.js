function randomizeNumber() {
  return new Promise((resolve, reject) => {
    const randomNumber = Math.floor(Math.random() * 100);
    console.log("Generated Number:", randomNumber);

    if (randomNumber % 2 === 0) {
      resolve(randomNumber);
    } else {
      reject(new Error("The number is odd"));
    }
  });
}

randomizeNumber()
  .then((evenNumber) => {
    console.log("Resolved with even number:", evenNumber);
  })
  .catch((error) => {
    console.log("Rejected with error:", error.message);
  });
