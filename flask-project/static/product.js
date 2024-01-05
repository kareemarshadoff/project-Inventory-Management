document.body.style = "background-color: var(--bs-dark);transition: 0.5s;"
const sun = "https://www.uplooder.net/img/image/55/7aa9993fc291bc170abea048589896cf/sun.svg";
const moon = "https://www.uplooder.net/img/image/2/addf703a24a12d030968858e0879b11e/moon.svg"

var theme = "dark";
const root = document.querySelector(":root");
const container = document.getElementsByClassName("theme-container")[0];
const themeIcon = document.getElementById("theme-icon");
container.addEventListener("click", setTheme);

function setTheme() {
    switch (theme) {
        case "dark":
            setLight();
            theme = "light";
            break;
        case "light":
            setDark();
            theme = "dark";
            break;
    }
}

function setLight() {
    root.style.setProperty(
        "--bs-dark",
        "linear-gradient(318.32deg, #c3d1e4 0%, #dde7f3 55%, #d4e0ed 100%)"
    );
    container.classList.remove("shadow-dark");
    setTimeout(() => {
        container.classList.add("shadow-light");
        themeIcon.classList.remove("change");
    }, 300);
    themeIcon.classList.add("change");
    themeIcon.src = sun;
}

function setDark() {
    root.style.setProperty("--bs-dark", "#212529");
    container.classList.remove("shadow-light");
    setTimeout(() => {
        container.classList.add("shadow-dark");
        themeIcon.classList.remove("change");
    }, 300);
    themeIcon.classList.add("change");
    themeIcon.src = moon;
}

var slNo = 1;

function addProduct() {
    var brand = document.getElementById('brand').value;
    var productName = document.getElementById('productName').value;
    var category = document.getElementById('category').value;
    var quantity = document.getElementById('quantity').value;
    var location = document.getElementById('location-select').value;
    var productPrice = document.getElementById('productPrice').value;

    if (!brand || !productName || !category || !quantity || !location || !productPrice) {
        alert('Please fill in all fields');
        return;
    }

    var table = document.getElementById('productTable').getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.rows.length);

    var cell0 = newRow.insertCell(0);
    var cell1 = newRow.insertCell(1);
    var cell2 = newRow.insertCell(2);
    var cell3 = newRow.insertCell(3);
    var cell4 = newRow.insertCell(4);
    var cell5 = newRow.insertCell(5);
    var cell6 = newRow.insertCell(6);
    var cell7 = newRow.insertCell(7);
    var cell8 = newRow.insertCell(8);

    cell0.innerHTML = slNo++;
    cell1.innerHTML = brand;
    cell2.innerHTML = productName;
    cell3.innerHTML = category;
    cell4.innerHTML = quantity;
    cell5.innerHTML = location;
    cell6.innerHTML = productPrice;
    cell7.innerHTML = getCurrentDate();
    cell8.innerHTML = getCurrentTime();

    document.getElementById('brand').value = '';
    document.getElementById('productName').value = '';
    document.getElementById('category').value = '';
    document.getElementById('quantity').value = '';
    document.getElementById('location-select').value = '';
    document.getElementById('productPrice').value = '';
}

function getCurrentDate() {
    var currentDate = new Date();
    return currentDate.toDateString();
}

function getCurrentTime() {
    var currentTime = new Date();
    return currentTime.toLocaleTimeString();
}