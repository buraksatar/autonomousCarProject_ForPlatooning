var app = angular.module("sampleApp", ["firebase"]);

// a factory to create a re-usable Profile object
// we pass in a username and get back their synchronized data as an object
app.factory("Profile", ["$firebaseObject",
  function($firebaseObject) {
    return function(username) {
      // create a reference to the database where we will store our data
      //var randomRoomId = Math.round(Math.random() * 100000000);
      var ref = new Firebase("https://testautonomous.firebaseio.com/");
      var profileRef = ref.child(username);

      // return it as a synchronized object
      return $firebaseObject(profileRef);
      //return $firebaseObject(profileRef);
    }
  }
]);

app.controller("ProfileCtrl", ["$scope", "Profile",
  function($scope, Profile) {
    // create a three-way binding to our Profile as $scope.profile
   Profile("autonomous").$bindTo($scope, "profile");
  }
]);
