function main()
{
	loadTopbar(document.getElementById("topbarcontainer"));
	getJson("containers").then(result => {listContainers(result["containers"]);});
}

function listContainers(containerIDArray)
{
	var containerContainer = document.getElementById("containerIds");

	for (let i = 0; i < containerIDArray.length; i++) {
		containerContainer.innerHTML += `<div onclick="chooseContainer(this, ${containerIDArray[i]})"> Container ${containerIDArray[i]} </div>`;
	}
	containerContainer.innerHTML += `<br><div> + </div>`; //TODO
}

function chooseContainer(card, number)
{
	var containerContainer = document.getElementById("containerIds");
	var cmc = document.getElementById("containerManagement");
	rmPdClInChilds(containerContainer);
	card.classList.add("picked");
	cmc.classList.remove("hide");

	postData("getContainer", {"id": number}).then(result => {updateManagement(result, number);});
}

function rmPdClInChilds(element)
{
	const childs = element.childNodes;

	for(i in childs) {
		try {
			childs[i].classList.remove("picked");
		} catch {
		}
	}
}

function updateManagement(container, id)
{
	var cmc = document.getElementById("containerManagement");

	document.getElementById("id").innerHTML = `ID: ${id}`;
	document.getElementById("sps").value = `${container['cD']['save_paths']}`;
	document.getElementById("lbu").innerHTML = `last backup: ${container['cD']['last_backup']}`;
	document.getElementById("bul").value = `${container['cD']['store_location']}`;
}

function save()
{
	var cmc = document.getElementById("containerManagement");
	var id = parseInt((document.getElementById("id").innerHTML).slice(4));
	var sps = document.getElementById("sps").value.split(",");
	var bul = document.getElementById("bul").value;

	pw = prompt("password");

	postData("update", {"id" : id, "sps" : sps, "bul" : bul, "pw" : pw}).then(result => { if(result["rt"] == false) {alert("wrong Password");} else {alert("saved");}});
}

function backup()
{
	var pw = prompt("password");
	var id = parseInt((document.getElementById("id").innerHTML).slice(4));
	var bud = `${String(new Date().getMonth() + 1).padStart(2, '0')}/${String(new Date().getDate()).padStart(2, '0')}/${new Date().getFullYear()} ${String(new Date().getHours()).padStart(2, '0')}:${String(new Date().getMinutes()).padStart(2, '0')}`;

	postData("backup", {"id" : id, "bud": bud, "pw" : pw}).then(result => { if(result["rt"] == false) {alert("wrong Password");} else {alert("backup made");}});
}

main();
