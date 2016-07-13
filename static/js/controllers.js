"use strict";

myApp.controller('tweetsController', function ($scope) {
    console.log($scope.tweets);
});

myApp.controller('usersController', function ($scope) {
    $scope.slicedTwoUsers = [];
    while ($scope.users.length) {
        $scope.slicedTwoUsers.push($scope.users.splice(0, 2));
    }
});

myApp.controller('hashtagsController', function ($scope) {
    
});

