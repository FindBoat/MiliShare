'use strict';

/* Controllers */

function IndexController($scope, $http, $location) {
	$scope.formData = {};
	$scope.processForm = function() {
		var channel = $scope.formData.channel;
		$location.path('/' + channel);
	};
}

function AboutController($scope) {

}

function PostListController($scope, Post) {
	var postsQuery = Post.get({}, function(posts) {
		$scope.posts = posts.objects;
	});
}

function CardController($scope, $routeParams, Cards, $timeout, $location) {
	$scope.channel = $routeParams.channel;
	Cards.get({channel: $scope.channel}, function(cards) {
		$scope.card = cards.data[0];
		if (!$scope.card.permanent) {
			startTimer();
		}
	});

	$scope.createCard = function() {
		var newCard = new Cards({
			channel: $scope.channel,
			content: $scope.formData.content
		});
		newCard.$save(function(card) {
			$location.path('/' + $scope.channel);
			$scope.card = card.data;
			startTimer();
		});
	};

	// Setting countdown timer.
	function startTimer() {
		$scope.hour = $scope.minute = $scope.second = 0;
		if ($scope.card && $scope.card.create_time) {
			var date = Date.parse($scope.card.create_time);
			var today = new Date();
			var secondsLeft =
				Math.round((date + 24 * 60 * 60 * 1000 - today) / 1000);

			if (secondsLeft > 0) {
				var countDown = function() {
					secondsLeft--;
					$scope.hour = Math.round(secondsLeft / 3600);
					$scope.minute = Math.round((secondsLeft % 3600) / 60);
					$scope.second = (secondsLeft % 3600) % 60;
					$timeout(countDown, 1000);
				}

				$timeout(countDown, 1000);
			}
		}
	}
}
