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

function terminalSubmitHW15(event) {
    if (event.keyCode === 13) {
        let commandLine = document.getElementById("command_line_hw15");
        let terminal = document.getElementById("terminal_hw15");

        commandLine.readOnly = true;

        let command = commandLine.value;
        let the_promise = null;

        pk = parseInt(command);

        if (command === "/usage/hw15") {
            the_promise = fetchUsageHW15();
        } else if (pk !== NaN) {
            the_promise = fetchAnimal(pk);
        }

        if (the_promise !== null) {
            the_promise.then(() => showCommandLinehw15())
        } else {
            let new_p = document.createElement("p");
            new_p.className = "terminal__p";
            let message = document.createTextNode("Unknown command. Try /usage/hw15 for help");
            new_p.appendChild(message);
            terminal.appendChild(new_p);
            showCommandLinehw15();
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

function showCommandLinehw15() {
    let terminal = document.getElementById("terminal_hw15");
    let commandLine = document.getElementById("command_line_hw15");

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
    commandLine.id = "command_line_hw15";
    commandLine.addEventListener("keypress", terminalSubmitHW15)

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

function makeErrorHW15(msg) {
    msg = document.createTextNode(msg || "Something went wrong...");
    let new_p = document.createElement("p");
    new_p.className = "terminal__p terminal__p_error";
    new_p.appendChild(msg);
    let terminal = document.getElementById("terminal_hw15");
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

function fetchUsageHW15() {

    let terminal = document.getElementById("terminal_hw15");

    return fetch('/usage/hw15', {method: 'GET', headers: {}})
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

function fetchAnimal(pk) {

    let terminal = document.getElementById("terminal_hw15");

    return fetch(`/animals/${pk}`, {method: 'GET', headers: {}})
        .then(response => {
            if (response.status !== 200) {
                return null;
            } else {
                return response.json()
            }
        }).then(data => {

            if (data === null) {
                makeErrorHW15();
            } else {
                let container_div = document.createElement("div");
                container_div.className = "animal__container";
                
                let animal_div = document.createElement("div");
                animal_div.className = "animal";

                // main

                let main_div = document.createElement("div");
                main_div.className = "animal__main";

                let main_table = document.createElement("table");
                main_table.className = "animal__table";
                
                let main_table_tr = document.createElement("tr");

                let main_table_tr_th_kind = document.createElement("th");
                main_table_tr_th_kind.textContent = "Тип";

                let main_table_tr_th_name = document.createElement("th");
                main_table_tr_th_name.textContent = "Кличка";

                let main_table_tr_th_birth = document.createElement("th");
                main_table_tr_th_birth.textContent = "Дата рождения";

                main_table_tr.appendChild(main_table_tr_th_kind);
                main_table_tr.appendChild(main_table_tr_th_name);
                main_table_tr.appendChild(main_table_tr_th_birth);

                let main_table_tr_values = document.createElement("tr");

                let main_table_tr_values_kind = document.createElement("td");
                main_table_tr_values_kind.textContent = data["animal"]["kind"];
                
                let main_table_tr_values_name = document.createElement("td");
                main_table_tr_values_name.textContent = data["animal"]["name"];

                let main_table_tr_values_birth = document.createElement("td");
                main_table_tr_values_birth.textContent = data["animal"]["birthday"];

                main_table_tr_values.appendChild(main_table_tr_values_kind);
                main_table_tr_values.appendChild(main_table_tr_values_name);
                main_table_tr_values.appendChild(main_table_tr_values_birth);

                main_table.appendChild(main_table_tr);
                main_table.appendChild(main_table_tr_values);

                main_div.appendChild(main_table);

                // breeds

                let breeds_div = document.createElement("div");
                breeds_div.className = "animal__breeds";

                let breeds_table = document.createElement("table");
                breeds_table.className = "animal__table";

                let breeds_table_headers = document.createElement("tr");

                let breeds_table_headers_breeds = document.createElement("th");
                breeds_table_headers_breeds.textContent = "Порода";

                breeds_table_headers.appendChild(breeds_table_headers_breeds);
                breeds_table.appendChild(breeds_table_headers);

                for (let breed in data["breeds"]) {
                    let breeds_table_values = document.createElement("tr");
                    let breeds_table_new_value = document.createElement("td");

                    breeds_table_new_value.textContent = data["breeds"][breed]["name"];

                    breeds_table_values.appendChild(breeds_table_new_value);

                    breeds_table.appendChild(breeds_table_values);
                }

                breeds_div.appendChild(breeds_table);

                // colors

                let colors_div = document.createElement("div");
                colors_div.className = "animal__colors";

                let colors_table = document.createElement("table");
                colors_table.className = "animal__table";

                let colors_table_headers = document.createElement("tr");

                let colors_table_headers_colors = document.createElement("th");
                colors_table_headers_colors.textContent = "Цвет";

                colors_table_headers.appendChild(colors_table_headers_colors);
                colors_table.appendChild(colors_table_headers);

                for (let color in data["colors"]) {
                    let colors_table_values = document.createElement("tr");
                    let colors_table_new_value = document.createElement("td");

                    colors_table_new_value.textContent = data["colors"][color]["name"];

                    colors_table_values.appendChild(colors_table_new_value);

                    colors_table.appendChild(colors_table_values);
                }

                colors_div.appendChild(colors_table);

                // animal

                animal_div.appendChild(main_div);
                animal_div.appendChild(breeds_div);
                animal_div.appendChild(colors_div);

                // outcomes

                let outcomes_div = document.createElement("div");
                outcomes_div.className = "animal__outcomes"

                let outcomes_table = document.createElement("table");
                outcomes_table.className = "animal__table";

                let outcomes_table_headers = document.createElement("tr");

                let outcomes_table_headers_year = document.createElement("th");
                outcomes_table_headers_year.textContent = "Год";

                let outcomes_table_headers_month = document.createElement("th");
                outcomes_table_headers_month.textContent = "Месяц";
                
                let outcomes_table_headers_program = document.createElement("th");
                outcomes_table_headers_program.textContent = "Программа";

                let outcomes_table_headers_status = document.createElement("th");
                outcomes_table_headers_status.textContent = "Статус";

                outcomes_table_headers.appendChild(outcomes_table_headers_year);
                outcomes_table_headers.appendChild(outcomes_table_headers_month);
                outcomes_table_headers.appendChild(outcomes_table_headers_program);
                outcomes_table_headers.appendChild(outcomes_table_headers_status);

                outcomes_table.appendChild(outcomes_table_headers);

                for (let outcome in data["outcomes"]) {
                
                    let outcomes_table_values = document.createElement("tr");
                    let outcomes_table_values_year = document.createElement("td");
                    let outcomes_table_values_month = document.createElement("td");
                    let outcomes_table_values_program = document.createElement("td");
                    let outcomes_table_values_status = document.createElement("td");

                    outcomes_table_values_year.textContent = data["outcomes"][outcome]["year"]
                    outcomes_table_values_month.textContent = data["outcomes"][outcome]["month"]
                    outcomes_table_values_program.textContent = data["outcomes"][outcome]["services"] || "Нет данных"
                    outcomes_table_values_status.textContent = data["outcomes"][outcome]["status"] || "Нет данных"

                    outcomes_table_values.appendChild(outcomes_table_values_year);
                    outcomes_table_values.appendChild(outcomes_table_values_month);
                    outcomes_table_values.appendChild(outcomes_table_values_program);
                    outcomes_table_values.appendChild(outcomes_table_values_status);

                    outcomes_table.appendChild(outcomes_table_values);
                
                }

                outcomes_div.appendChild(outcomes_table);

                // container

                container_div.appendChild(animal_div);
                container_div.appendChild(outcomes_div);

                terminal.appendChild(container_div);
                
            }
        });
}

window.onload = () => {

    fetchUsageHW14().then(() => showCommandLine());
    fetchUsageHW15().then(() => showCommandLinehw15());
    
}