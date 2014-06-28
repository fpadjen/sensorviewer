var myAppModule = angular.module('myApp', [ 'ui.chart', 'services', 'controllers' ])

var controllers = angular.module('controllers', []);

controllers.controller('SensorCtrl', ['$scope', 'Point', '$http', function($scope, Point, $http) {
	$scope.chart = [[[1403993896.091306 * 1000.,1], [1403995896.091306 * 1000.,2]]]

	$scope.chartOptions = {
		sortData : true,
		title : 'Sensor 1',
		axes : {
			xaxis : {
				renderer : $.jqplot.DateAxisRenderer,
				tickOptions : {
					formatString : '%Y-%m-%d',
					angle : 15
				},
			},
		}
	}

	function success(data, textStatus, jqXHR) {
		var plotable = [[]]
		for (i in data[0]) {
			plotable[0].push(data[0][i])
		}
        $.jqplot('chartdiv', plotable, $scope.chartOptions).replot();
	}

	function error(data, status, headers, config) {
		console.log(status);
		console.log(data);
	}

	function make_request() {
		console.log('executed')
		var data = Point.query();
		data.$promise.then(success)
		setInterval(make_request, 60000)
	}

	$.jqplot('chartdiv', $scope.chart, $scope.chartOptions);
	make_request();
}]);