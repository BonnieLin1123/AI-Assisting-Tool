chrome.runtime.onInstalled.addListener(() => {
    console.log("ADHD Assistant Installed!");
});

chrome.runtime.onStartup.addListener(() => {
    console.log("ADHD Assistant Started!");
});

// Keep service worker alive
chrome.alarms.create("keepAlive", { delayInMinutes: 5, periodInMinutes: 5 });

chrome.alarms.onAlarm.addListener((alarm) => {
    if (alarm.name === "keepAlive") {
        console.log("Keeping service worker alive");
    }
});

// Handle messages from popup.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "startTimer") {
        chrome.alarms.create("focusAlarm", { delayInMinutes: message.duration });
    }
});

chrome.alarms.onAlarm.addListener((alarm) => {
    if (alarm.name === "focusAlarm") {
        chrome.notifications.create({
            type: "basic",
            iconUrl: "icon.png",
            title: "Focus Session Over!",
            message: "Time for a break!"
        });
    }
});
