/**
 * Created by young on 1/19/15.
 */
angular.module('animateApp', ['ngAnimate'])
    .controller('slideCtrl', slideCtrl);


function slideCtrl($scope, $interval){

    $scope.quote = 1;
    $interval( function(){
        $scope.quote = ($scope.quote <  $scope.quotemax )? $scope.quote+1 : 1;
    }, 10000);
}