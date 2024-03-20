// Calculate the age of the user
const ageCalculate = () => {
    // Get the date of today
    const today = new Date();
  
    // Get the user-input birth date
    const inputDate = new Date(document.getElementById("date-input").value);
  
    // Convert dates to milliseconds
    const birthTime = inputDate.getTime();
    const currentTime = today.getTime();
  
    // Check if birth date is in the future
    if (birthTime > currentTime) {
      alert("Wohoo!!! Not Born Yet!!!");
      displayResult("-", "-", "-");
      return;
    }
  
    // Calculate the time difference in milliseconds
    const diffTime = currentTime - birthTime;
  
    // Calculate from the time difference
    const years = Math.floor(diffTime / (1000 * 60 * 60 * 24 * 365));
    const months = Math.floor(
      (diffTime % (1000 * 60 * 60 * 24 * 365)) / (1000 * 60 * 60 * 24 * 30.44)
    );
    const days = Math.floor(
      (diffTime % (1000 * 60 * 60 * 24 * 30.44)) / (1000 * 60 * 60 * 24)
    );
  
    // Display the calculated age
    displayResult(days, months, years);
  };
  
  // Display the age result
  const displayResult = (days, months, years) => {
    document.getElementById("years").textContent = years;
    document.getElementById("months").textContent = months;
    document.getElementById("days").textContent = days;
  };
  
  // The button click event
  document.getElementById("calc-age-btn").addEventListener("click", ageCalculate);