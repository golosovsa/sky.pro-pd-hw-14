function terminalSubmit(event) {

    if (event.keyCode === 13) {

        let commandLine = document.getElementById("command_line");
        let terminal = document.getElementById("terminal");

        commandLine.readOnly = true;

        let command = commandLine.value;
        let the_promise = null;

        if (command === "/usage/hw14") {
            the_promise = fetchUsageHW14()
        } else if (command.startsWith("/movie/") && !command.includes("/to/")) {
            the_promise = fetchMovieByTitle(command);
        } else if (command.startsWith("/movie/") && command.includes("/to/")) {
            the_promise = fetchMoviesByRange(command);
        } else if (command.startsWith("/rating/")) {
            the_promise = fetchMoviesByRating(command);
        } else if (command.startsWith("/genre/")) {
            the_promise = fetchMoviesByGenre(command);
        } else if (command.startsWith("/together/")) {
            the_promise = fetchActorsPlaysTogetherWith(command);
        } else if (command.startsWith("/search/")) {
            the_promise = fetchSearch(command);
        }

        if (the_promise !== null) {
            the_promise.then(() => showCommandLine())
        } else {
            let new_p = document.createElement("p");
            new_p.className = "terminal__p";
            let message = document.createTextNode("Unknown command. Try /usage/hw14 for help");
            new_p.appendChild(message);
            terminal.appendChild(new_p);
            showCommandLine();
        }
    }
}

function showCommandLine() {
    let terminal = document.getElementById("terminal");
    let commandLine = document.getElementById("command_line");

    if (commandLine !== null) {
        let oldCommandLine = document.createElement("p");
        oldCommandLine.className = "terminal__p terminal__p_last"
        oldCommandLine.textContent = commandLine.value;
        commandLine.parentNode.replaceChild(oldCommandLine, commandLine);
        commandLine.remove();
    }

    commandLine = document.createElement("textarea");
    commandLine.rows = 6;
    commandLine.className = "terminal__command-line";
    commandLine.id = "command_line";
    commandLine.addEventListener("keypress", terminalSubmit)

    terminal.appendChild(commandLine)
}

function makeError(msg) {
    msg = document.createTextNode(msg || "Something went wrong...");
    let new_p = document.createElement("p");
    new_p.className = "terminal__p terminal__p_error";
    new_p.appendChild(msg);
    let terminal = document.getElementById("terminal");
    terminal.appendChild(new_p);
}

function fetchUsageHW14() {

    let terminal = document.getElementById("terminal");

    return fetch('/usage/hw14', {method: 'GET', headers: {}})
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

function fetchMovieByTitle(uri) {
    let terminal = document.getElementById("terminal");

    return fetch(uri, {method: 'GET', headers: {}})
        .then(response => {
            if (response.status !== 200) {
                return null;
            } else {
                return response.json()
            }
        }).then(data => {

            if (data === null) {
                makeError();
            } else {
                for (let p in data) {

                    let new_p = document.createElement("p");
                    let message = document.createTextNode(p + ": " + data[p]);

                    new_p.className = "terminal__p";
                    new_p.appendChild(message);

                    terminal.appendChild(new_p);
                }
            }
        })

}

function fetchMoviesByRange(uri) {
    let terminal = document.getElementById("terminal");

    return fetch(uri, {method: 'GET', headers: {}})
        .then(response => {
            if (response.status !== 200) {
                return null;
            } else {
                return response.json()
            }
        }).then(data => {

            if (data === null) {
                makeError();
            } else {
                for (let p in data) {

                    let new_p = document.createElement("p");
                    let message = document.createTextNode(p + ") " + data[p]["title"] + ", " + data[p]["release_year"]);

                    new_p.className = "terminal__p";
                    new_p.appendChild(message);

                    terminal.appendChild(new_p);
                }
            }
        });
}

function fetchMoviesByRating(uri) {
    let terminal = document.getElementById("terminal");

    return fetch(uri, {method: 'GET', headers: {}})
        .then(response => {
            if (response.status !== 200) {
                return null;
            } else {
                return response.json()
            }
        }).then(data => {

            if (data === null) {
                makeError();
            } else {
                for (let p in data) {

                    let new_p = document.createElement("p");
                    let message = document.createTextNode(
                        p + ") "
                        + data[p]["title"]
                        + ", " + data[p]["rating"]
                        + ", " + data[p]["description"].slice(0, 46) + " ...");

                    new_p.className = "terminal__p";
                    new_p.appendChild(message);
                    new_p.title = data[p]["description"];

                    terminal.appendChild(new_p);
                }
            }
        });
}

function fetchMoviesByGenre(uri) {

    let terminal = document.getElementById("terminal");

    return fetch(uri, {method: 'GET', headers: {}})
        .then(response => {
            if (response.status !== 200) {
                return null;
            } else {
                return response.json()
            }
        }).then(data => {

            if (data === null) {
                makeError();
            } else {
                for (let p in data) {

                    let new_p = document.createElement("p");
                    let message = document.createTextNode(
                        p + ") "
                        + data[p]["title"]
                        + ", " + data[p]["description"].slice(0, 46) + " ...");

                    new_p.className = "terminal__p";
                    new_p.appendChild(message);
                    new_p.title = data[p]["description"];

                    terminal.appendChild(new_p);
                }
            }
        });
}

function fetchActorsPlaysTogetherWith(uri) {

    let terminal = document.getElementById("terminal");

    return fetch(uri, {method: 'GET', headers: {}})
        .then(response => {
            if (response.status !== 200) {
                return null;
            } else {
                return response.json()
            }
        }).then(data => {

            if (data === null) {
                makeError();
            } else {
                for (let p in data) {

                    let new_p = document.createElement("p");
                    let message = document.createTextNode(
                        p + ") "
                        + data[p]["actor"]
                        + ", plays " + data[p]["total"] + " times"
                    );

                    new_p.className = "terminal__p";
                    new_p.appendChild(message);

                    terminal.appendChild(new_p);
                }
            }
        });
}

function fetchSearch(uri) {

        let terminal = document.getElementById("terminal");

    return fetch(uri, {method: 'GET', headers: {}})
        .then(response => {
            if (response.status !== 200) {
                return null;
            } else {
                return response.json()
            }
        }).then(data => {

            if (data === null) {
                makeError();
            } else {
                for (let p in data) {

                    let new_p = document.createElement("p");
                    let message = document.createTextNode(
                        p + ") "
                        + data[p]["title"]
                        + ", " + data[p]["description"].slice(0, 46) + " ...");

                    new_p.className = "terminal__p";
                    new_p.appendChild(message);
                    new_p.title = data[p]["description"];

                    terminal.appendChild(new_p);
                }
            }
        });
}

window.onload = () => {

    fetchUsageHW14().then(() => showCommandLine());
}