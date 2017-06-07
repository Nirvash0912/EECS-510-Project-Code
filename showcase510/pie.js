$(document).ready(function() {
	var pie = new d3pie("pieChart", {
		"header": {
			"title": {
				"text": "Distribution of Sentiment",
				"fontSize": 24,
				"font": "open sans"
			},
			"subtitle": {
				"color": "#999999",
				"fontSize": 12,
				"font": "open sans"
			},
			"titleSubtitlePadding": 10
		},
		"footer": {
			"color": "#999999",
			"fontSize": 10,
			"font": "open sans",
			"location": "bottom-left"
		},
		"size": {
			"canvasWidth": 590,
			"pieInnerRadius": "30%",
			"pieOuterRadius": "80%"
		},
		"data": {
			"sortOrder": "value-desc",
			"content": [
				{
					"label": "Positive",
					"value": 1328,
					"color": "#228835"
				},
				{
					"label": "Negative",
					"value": 33691,
					"color": "#2081c1"
				},
				{
					"label": "Neutral",
					"value": 48384,
					"color": "#efefef"
				}
			]
		},
		"labels": {
			"mainLabel": {
				"fontSize": 20
			},
			"percentage": {
				"color": "#ffffff",
				"fontSize": 25,
				"decimalPlaces": 0
			},
			"value": {
				"color": "#adadad",
				"fontSize": 20
			},
			"lines": {
				"enabled": true,
				"style": "straight"
			},
			"truncation": {
				"enabled": true
			}
		},
		"effects": {
			"load": {
				"effect": "none"
			},
			"pullOutSegmentOnClick": {
				"effect": "linear",
				"speed": 400,
				"size": 8
			}
		},
		"misc": {
			"gradient": {
				"enabled": true,
				"percentage": 100
			}
		}
	});

	var pie_pn = new d3pie("pieChart_pn", {
		"header": {
			"title": {
				"text": "Distribution of Sentiment (Only Positive and Negative)",
				"fontSize": 24,
				"font": "open sans"
			},
			"subtitle": {
				"color": "#999999",
				"fontSize": 12,
				"font": "open sans"
			},
			"titleSubtitlePadding": 10
		},
		"footer": {
			"color": "#999999",
			"fontSize": 10,
			"font": "open sans",
			"location": "bottom-left"
		},
		"size": {
			"canvasWidth": 590,
			"pieInnerRadius": "30%",
			"pieOuterRadius": "80%"
		},
		"data": {
			"sortOrder": "value-desc",
			"content": [
				{
					"label": "Positive",
					"value": 1328,
					"color": "#228835"
				},
				{
					"label": "Negative",
					"value": 33691,
					"color": "#2081c1"
				}
			]
		},
		"labels": {
			"mainLabel": {
				"fontSize": 20
			},
			"percentage": {
				"color": "#ffffff",
				"fontSize": 25,
				"decimalPlaces": 0
			},
			"value": {
				"color": "#adadad",
				"fontSize": 20
			},
			"lines": {
				"enabled": true,
				"style": "straight"
			},
			"truncation": {
				"enabled": true
			}
		},
		"effects": {
			"load": {
				"effect": "none"
			},
			"pullOutSegmentOnClick": {
				"effect": "linear",
				"speed": 400,
				"size": 8
			}
		},
		"misc": {
			"gradient": {
				"enabled": true,
				"percentage": 100
			}
		}
	});
});

