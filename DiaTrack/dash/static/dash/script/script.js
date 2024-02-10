addEventListener('DOMContentLoaded', function () {

let insulin = document.getElementById("insulin");
let glucose = document.getElementById("glucose");
let insulinChanges = document.getElementById("insulin-changes");
let meal = document.getElementById("meal");
let reminders = document.getElementById("reminders");
let cgm = document.getElementById("cgm");

// check if the element exists before adding the event listener
if (insulin != null)
insulin.addEventListener("click", ShowHideInsulin);

if (glucose != null)
glucose.addEventListener("click", ShowHideGlucose);

if (insulinChanges != null)
insulinChanges.addEventListener("click", ShowHideInsulinChanges);

if (meal != null)
meal.addEventListener("click", ShowHideMeal);

if (reminders != null)
reminders.addEventListener("click", ShowHideReminders);

if (cgm != null)
cgm.addEventListener("click", ShowHideCGM);

})



// Function to show/hide the body of the tables
function ShowHideInsulin() {
    document.getElementById("insulin-body").classList.toggle("hide")
}

function ShowHideGlucose() {
    document.getElementById("glucose-body").classList.toggle("hide")
}

function ShowHideInsulinChanges() {
    document.getElementById("insulin-changes-body").classList.toggle("hide")
}

function ShowHideMeal() {
    document.getElementById("meal-body").classList.toggle("hide")
}

function ShowHideReminders() {
    document.getElementById("reminders-body").classList.toggle("hide")
}

function ShowHideCGM() {
    document.getElementById("cgm-body").classList.toggle("hide")
}