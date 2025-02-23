console.log("ADHD Assistant content script loaded!");

// List of distracting sites to block
const blockedSites = ["facebook.com", "youtube.com", "twitter.com"];

if (blockedSites.some(site => window.location.href.includes(site))) {
    document.body.innerHTML = `<h1>Blocked! Stay focused! 🚀</h1>`;
}

// Listen for blockSites command
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "blockSites") {
        document.body.innerHTML = `<h1>Blocked! Stay focused! 🚀</h1>`;
    }
});
