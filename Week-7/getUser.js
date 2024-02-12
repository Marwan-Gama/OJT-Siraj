fetch("https://jsonplaceholder.typicode.com/users")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((users) => {
    const firstUser = users[0];
    console.log("Company Name:", firstUser.company.name);
  })
  .catch((error) => {
    console.error("There was a problem with your fetch operation:", error);
  });
