document.addEventListener("DOMContentLoaded", function () {
    const stateSelect = document.getElementById("state");
    const citySelect = document.getElementById("city");

    if (!stateSelect || !citySelect) return;

    const stateCities = {
        "Delhi": ["New Delhi", "Dwarka", "Saket", "Vasant Kunj", "Rohini"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Thane"],
        "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot"],
        "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Ajmer"],
        "Uttar Pradesh": ["Noida", "Lucknow", "Ghaziabad", "Kanpur", "Agra"],
        "Karnataka": ["Bengaluru", "Mysuru", "Mangaluru", "Hubli"],
        "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Salem"],
        "Telangana": ["Hyderabad", "Warangal"],
        "West Bengal": ["Kolkata", "Howrah", "Darjeeling"]
    };

    function loadCities() {
        const selectedState = stateSelect.value;
        const previouslySelectedCity = citySelect.getAttribute("data-selected");

        // Clear existing options
        citySelect.innerHTML = '<option value="">Select City</option>';

        if (selectedState && stateCities[selectedState]) {
            stateCities[selectedState].forEach(city => {
                const option = document.createElement("option");
                option.value = city;
                option.textContent = city;

                // Pre-select if matches (for Edit Page)
                if (city === previouslySelectedCity) {
                    option.selected = true;
                }

                citySelect.appendChild(option);
            });
        }
    }

    stateSelect.addEventListener("change", loadCities);

    // Trigger on load if state is already selected (Edit Page case)
    if (stateSelect.value) {
        loadCities();
    }
});