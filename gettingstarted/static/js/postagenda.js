angular.module('addAgenda', []).config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken'
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
});

angular.module('addAgenda', [])
.controller('AgendaController', function($scope, $http) {
  $scope.agendas = [];
  
  $scope.addAgenda = function() {
    $scope.agendas.push({text:$scope.agendaText, done:false});
    $scope.agendaText = '';
    $http.post('/agenda', {data:$scope.agendaText}
         ).
      success(function(data, status, headers, config) {
      console.log(data);
      // this callback will be called asynchronously
      // when the response is available
    }).
      error(function(data, status, headers, config) {
      console.log(data);
      // called asynchronously if an error occurs
      // or server returns response with an error status.
    });
  };
  
  $scope.remaining = function() {
    var count = 0;
    angular.forEach($scope.agendas, function(agenda) {
      count += agenda.done ? 0 : 1;
    });
    return count;
  };
  
  $scope.archive = function() {
    var oldAgendas = $scope.agendas;
    $scope.agendas = [];
    angular.forEach(oldAgendas, function(agenda) {
      if (!agenda.done) $scope.agendas.push(agenda);
    });
  };
});