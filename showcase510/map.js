function tooltipHtml(n, d){	/* function to create html content string in tooltip div. */
	return "<h4>"+n+"</h4><table>"+
		"<tr><td>count</td><td>"+(d.count)+"</td></tr>"+
		"</table>";
}

var stat_population = {
	"CA": 39250017,
	"TX": 27862596,
	"FL": 20612439,
	"NY": 19745289,
	"PA": 12802503,
	"IL": 12801539,
	"OH": 11614373,
	"GA": 10310371,
	"NC": 10146788,
	"MI": 9928301,
	"NJ": 8944469,
	"VA": 8411808,
	"WA": 7288000,
	"AZ": 6931071,
	"MA": 6811779,
	"TN": 6651194,
	"IN": 6633053,
	"MO": 6093000,
	"MD": 6016447,
	"WI": 5778708,
	"CO": 5540545,
	"MN": 5519952,
	"SC": 4961119,
	"AL": 4863300,
	"LA": 4681666,
	"KY": 4436974,
	"OR": 4093465,
	"OK": 3923561,
	"CT": 3576452,
	"IA": 3134693,
	"UT": 3051217,
	"MS": 2988726,
	"AR": 2988248,
	"NV": 2940058,
	"KS": 2907289,
	"NM": 2081015,
	"NE": 1907116,
	"WV": 1831102,
	"ID": 1683140,
	"HI": 1428557,
	"NH": 1334795,
	"ME": 1331479,
	"RI": 1056426,
	"MT": 1042520,
	"DE": 952065,
	"SD": 865454,
	"ND": 757952,
	"AK": 741894,
	"VT": 624594,
	"WY": 585501
};

function getQueryVariable(variable) {
    var query = decodeURIComponent(window.location.search.substring(1));
    var vars = query.split("&");
    for (var i=0;i<vars.length;i++) {
        var pair = vars[i].split("=");
        if(pair[0] == variable){
            var replaced = pair[1].split('+').join(' ');
            return replaced;
        }
    }
    return undefined;
}

function drawMap(datafile){
	var sampleData ={};
	var states = [];
	var counts = [];
	var max = 0;
	d3.csv(datafile, function(data) {
		data.forEach(function(d){
  			states.push(d.state)
			counts.push(parseInt(d.count));
		});
		var temp_index = 0;
  		var weights = [];
  		states.forEach(function(d){
  			weights.push(counts[temp_index] / stat_population[d])
  			temp_index ++;
  		});

  		max = d3.max(weights)

  		console.log(weights)

  		var i = 0
  		sampleData["DC"] = {count:0, color:d3.interpolate("#36e275", "#e23636")(0 / max)}
		states.forEach(function(d){
			sampleData[d] = {count:counts[i], color:d3.interpolate("#36e275", "#e23636")(weights[i] / max)};
			i++;
		});

		// console.log(sampleData)

		/* draw states on id #statesvg */	
		uStates.draw("#statesvg", sampleData, tooltipHtml);
	
		d3.select(self.frameElement).style("height", "600px"); 
	});
}

$(document).ready(function() {
	var mapType = getQueryVariable("type");
	var month = getQueryVariable("month");

	if(mapType.localeCompare("overall") == 0){
		var datafile = "./data/location_stat_overall.csv";
		document.getElementById("map-type").innerHTML = "<h4>Overall</h4>";
		drawMap(datafile);
	} else {
		var datafile = "./data/location_stat_months" + month + ".csv"
		var month_string = "";
		switch(parseInt(month)) {
			case 1: month_string = "January";break;
			case 2: month_string = "February";break;
			case 3: month_string = "March";break;
			case 4: month_string = "April";break;
			case 5: month_string = "May";break;
			case 6: month_string = "June";break;
			case 7: month_string = "July";break;
			case 8: month_string = "August";break;
			case 9: month_string = "September";break;
			case 10: month_string = "October";break;
			case 11: month_string = "November";break;
			case 12: month_string = "December";break;
		}
		document.getElementById("map-type").innerHTML = "<h4>" + month_string + "</h4>";
		drawMap(datafile);
	}
});