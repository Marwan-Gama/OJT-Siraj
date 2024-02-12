// Function to generate an array of 10 students
function generateStudents(callback) {
  const students = [];
  for (let i = 0; i < 10; i++) {
    const cityId = Math.floor(Math.random() * 3) + 1; // Generate a random city ID between 1 and 3
    const student = {
      id: i + 1,
      name: `Student ${i + 1}`,
      course: `Course ${i + 1}`,
      address: {
        city: `City ${cityId}`, // Use the random city ID
      },
    };
    students.push(student);
  }
  callback(students);
}

// Function to count students from each city after a 2-second delay
function countStudentsByCity(students, printFunction) {
  setTimeout(() => {
    const cityStudents = {}; // Object to store students by city
    students.forEach((student) => {
      const city = student.address.city;
      if (cityStudents[city]) {
        cityStudents[city].push(student); // Add student to existing city array
      } else {
        cityStudents[city] = [student]; // Create new city array with student
      }
    });
    // Call the print function to print cities and their corresponding students
    printFunction(cityStudents);
  }, 2000);
}

// Function to print cities and their corresponding students
function printCitiesAndStudents(cityStudents) {
  for (const city in cityStudents) {
    console.log(`${city}:`);
    cityStudents[city].forEach((student) => {
      console.log(`  ${student.name}`);
    });
  }
}

// Call the generateStudents function to generate students and then count students by city
generateStudents((students) => {
  countStudentsByCity(students, printCitiesAndStudents);
});
