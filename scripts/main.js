import { dataSeries } from "./dataSeries.js";
var seriesTbody = document.getElementById('series');
var avgSeasons = document.getElementById("avg-seasons");
renderSeriesInTable(dataSeries);
avgSeasons.innerHTML = "".concat(getAvgSeasons(dataSeries));
function renderSeriesInTable(series) {
    console.log('Desplegando series');
    series.forEach(function (serie) {
        var trElement = document.createElement("tr");
        var tdID = document.createElement("td");
        tdID.innerHTML = serie.id.toString();
        trElement.appendChild(tdID);
        var tdName = document.createElement("td");
        tdName.innerHTML = "<a href=\"#\" class=\"serie-name\">".concat(serie.name, "</a>");
        trElement.appendChild(tdName);
        var tdChannel = document.createElement("td");
        tdChannel.innerHTML = serie.channel;
        trElement.appendChild(tdChannel);
        var tdSeasons = document.createElement("td");
        tdSeasons.innerHTML = serie.seasons.toString();
        trElement.appendChild(tdSeasons);
        seriesTbody.appendChild(trElement);
    });
}
function getAvgSeasons(series) {
    var sum = 0;
    var cont = series.length;
    series.forEach(function (serie) { return sum = sum + serie.seasons; });
    console.log("Valor sum: " + sum);
    console.log("Valor cont: " + cont);
    var avg = sum / cont;
    return avg;
}
