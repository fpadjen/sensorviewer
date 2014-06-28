var services = angular.module('services', ['ngResource']);

services.factory('Point', ['$resource',
  function($resource){
    return $resource('points/', {}, {
      query: {method:'GET', isArray:true}
    });
  }]);