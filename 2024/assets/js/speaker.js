function showSpeakers(data) {
    //console.log('-= showSpeakers() =-')
    //var members = data.members;
    var members = data;
    var remainder = 0;

    var content = '';
    var byName = members.slice(0);
    byName.sort(function (a, b) {
        var x = a["Title"].toLowerCase();
        var y = b["Title"].toLowerCase();
        return x < y ? -1 : x > y ? 1 : 0;
    });
    //console.log('byName:', byName);
    for (var index in byName) {
        //console.log(' * key:', index, byName[index]);
        if (typeof byName[index] === "undefined") {
            continue;
        }
        //console.log(index,') name:', byName[index]["Your name"]);
        var title = byName[index]["Title"];
        var titleID = title.replace(/[ \.,_\"\':]/gi, "-");
        titleID = titleID.replace(/--*/g, "-");
        titleID = titleID.replace(/^-/, "");
        titleID = titleID.replace(/!/, "-");
        titleID = titleID.replace(/\?/, "-");
        titleID = titleID.replace(/\(/, "-");
        titleID = titleID.replace(/\)/, "-");
        titleID = titleID.replace(/&/, "-");
        titleID = titleID.toLowerCase();

        content += `<div class="modal fade" id="` + titleID + `" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                      <div class="modal-dialog modal-lg" role="document">
                        <div class="modal-content">
                          <div class="modal-body">
                            <div id="card">
                              <h5 id="h1card">` + byName[index]["Title"] + `</h5>
			      <div class="image-crop">\n`;
        if (byName[index]["Image"]) {
            //console.log(byName[index]["Images"]);
            content += `<img id="avatar" src="` + byName[index]["Image"] + `">`
        }
	content += `          </div>
                              <div id="abstract">
                                <h3 id="h2card">` + byName[index]["Name"] + `</h3>
                                <p>` + byName[index]["Abstract"] + `</p>
                                <p id="abstract">Presentation type: <b>` + byName[index]["Type"] + `</b></p>
                                <h3 id="h3card">About speaker</h3>
                                <p>` + byName[index]["Biography"] + `</p>
                              </div>
                            </div>
                          </div>
                          <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                          </div>
                        </div>
                      </div>
                    </div>`;
    }
    speakersHTML.innerHTML += content;
    //console.log('-= end of showSpeakers() =-')
}

// source: https://howtocreateapps.com/fetch-and-display-json-html-javascript/
fetch("speakers.json")
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        showSpeakers(data);
    })
    .catch(function (err) {
        console.log('ERROR:', err);
    });
var speakersHTML = document.getElementById("show-speakers");
