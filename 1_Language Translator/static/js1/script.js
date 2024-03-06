// Selecting elements from the DOM
const fromText = document.querySelector(".from-text"); // Select an element with class "from-text"
const toText = document.querySelector(".to-text"); // Select an element with class "to-text"
const exchageIcon = document.querySelector(".exchange"); // Select an element with class "exchange"
const selectTag = document.querySelectorAll("select"); // Select all <select> elements on the page
const icons = document.querySelectorAll(".row i"); // Select all <i> elements with class "row"
const translateBtn = document.querySelector("button"); // Select the first <button> element on the page

// Populating select elements with options based on the 'countries' object
selectTag.forEach((tag, id) => {
    for (let country_code in countries) {
        // Set the 'selected' attribute for specific options based on conditions
        let selected = id == 0 ? country_code == "en-GB" ? "selected" : "" : country_code == "hi-IN" ? "selected" : "";
        // Create an <option> element with the selected attribute and country code as the value
        let option = `<option ${selected} value="${country_code}">${countries[country_code]}</option>`;
        // Insert the option element into the select element
        tag.insertAdjacentHTML("beforeend", option);
    }
});

// Add an event listener to the exchangeIcon for swapping text and select values
exchageIcon.addEventListener("click", () => {
    // Swap the values of the 'fromText' and 'toText' elements
    let tempText = fromText.value;
    let tempLang = selectTag[0].value;
    fromText.value = toText.value;
    toText.value = tempText;
    // Swap the values of the first and second select elements
    selectTag[0].value = selectTag[1].value;
    selectTag[1].value = tempLang;
});

// Add an event listener to the 'fromText' input for clearing 'toText' when 'fromText' is empty
fromText.addEventListener("keyup", () => {
    if (!fromText.value) {
        toText.value = "";
    }
});

// Add an event listener to the translateBtn for translating text using an API
translateBtn.addEventListener("click", () => {
    let text = fromText.value.trim();
    let translateFrom = selectTag[0].value;
    let translateTo = selectTag[1].value;
    if (!text) return; // Exit if 'text' is empty
    toText.setAttribute("placeholder", "Translating..."); // Set a placeholder text
    let apiUrl = `https://api.mymemory.translated.net/get?q=${text}&langpair=${translateFrom}|${translateTo}`;
    // Fetch data from the translation API and update 'toText' with the translation
    fetch(apiUrl)
        .then(res => res.json())
        .then(data => {
            toText.value = data.responseData.translatedText;
            data.matches.forEach(data => {
                if (data.id === 0) {
                    toText.value = data.translation;
                }
            });
            toText.setAttribute("placeholder", "Translation"); // Reset the placeholder text
        });
});

// Add event listeners to icons for copying or speaking text
icons.forEach(icon => {
    icon.addEventListener("click", ({target}) => {
        if (!fromText.value || !toText.value) return; // Exit if 'fromText' or 'toText' is empty
        if (target.classList.contains("fa-copy")) {
            if (target.id == "from") {
                // Copy 'fromText' to the clipboard
                navigator.clipboard.writeText(fromText.value);
            } else {
                // Copy 'toText' to the clipboard
                navigator.clipboard.writeText(toText.value);
            }
        } else {
            let utterance;
            if (target.id == "from") {
                // Create a speech synthesis utterance for 'fromText'
                utterance = new SpeechSynthesisUtterance(fromText.value);
                utterance.lang = selectTag[0].value;
            } else {
                // Create a speech synthesis utterance for 'toText'
                utterance = new SpeechSynthesisUtterance(toText.value);
                utterance.lang = selectTag[1].value;
            }
            // Speak the utterance
            speechSynthesis.speak(utterance);
        }
    });
});
