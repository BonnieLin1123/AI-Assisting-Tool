document.addEventListener("DOMContentLoaded", function () {
    console.log("Popup loaded!");

    // Get elements safely
    const focusButton = document.getElementById("focusMode");
    const blockButton = document.getElementById("blockSites");
    const statusText = document.getElementById("status");

    if (focusButton) {
        focusButton.addEventListener("click", () => {
            chrome.runtime.sendMessage({ action: "startTimer", duration: 25 });
            if (statusText) {
                statusText.innerText = "Focus Mode started!";
            }
        });
    } else {
        console.error("focusMode button not found");
    }

    if (blockButton) {
        blockButton.addEventListener("click", () => {
            chrome.runtime.sendMessage({ action: "blockSites" });
            alert("Blocking distracting websites!");
        });
    } else {
        console.error("blockSites button not found");
    }
});
