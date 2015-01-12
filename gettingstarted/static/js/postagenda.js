angular.module('addAgenda', [])
  .controller('AgendaController', ['$scope', function($scope) {
    $scope.agendas = [];
 
    $scope.addAgenda = function() {
      $scope.agendas.push({text:$scope.agendaText, done:false});
      $scope.agendaText = '';
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
  }]);