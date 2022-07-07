function fetchUsageHW14() {

    let terminal = document.getElementById("terminal");

    fetch('/usage/hw14', {method: 'GET', headers: {}})
        .then(response => response.json())
        .then(data => {
            for (let p in data) {
                let new_p = document.createElement("p");
                new_p.className = "terminal__p";
                if ("route" in data[p]) {
                    let new_span = document.createElement("span");
                    new_span.className = "terminal__p terminal__p_highlight";
                    new_span.textContent += data[p]["route"];
                    new_p.appendChild(new_span);
                }
                let message = document.createTextNode(data[p]["message"]);
                new_p.appendChild(message);
                terminal.appendChild(new_p);
            }
        })
}

window.onload = () => {

    fetchUsageHW14()

    // let test_elem = document.createElement("h1")
    // test_elem.textContent = "Hello world"
    // terminal.appendChild(test_elem)
}