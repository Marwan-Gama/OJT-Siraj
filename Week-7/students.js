function generateStudents(callback) {
  const students = [];
  for (let i = 0; i < 10; i++) {
    const cityId = Math.floor(Math.random() * 3) + 1;
    const student = {
      id: i + 1,
      name: `Student ${i + 1}`,
      course: `Course ${i + 1}`,
      address: {
        city: `City ${cityId}`,
      },
    };
    students.push(student);
  }
  callback(students);
}

function countStudentsByCity(students, printFunction) {
  setTimeout(() => {
    const cityStudents = {};
    students.forEach((student) => {
      const city = student.address.city;
      if (cityStudents[city]) {
        cityStudents[city].push(student);
      } else {
        cityStudents[city] = [student];
      }
    });

    printFunction(cityStudents);
  }, 2000);
}

function printCitiesAndStudents(cityStudents) {
  for (const city in cityStudents) {
    console.log(`${city}:`);
    cityStudents[city].forEach((student) => {
      console.log(`  ${student.name}`);
    });
  }
}

generateStudents((students) => {
  countStudentsByCity(students, printCitiesAndStudents);
});
