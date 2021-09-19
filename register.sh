docker build . -t $BUILD_IMAGE_LOCAL
export CR="anubhavgarg/olist"
docker tag $BUILD_IMAGE_LOCAL $CR:$GITHUB_SHA
docker push $CR::$GITHUB_SHA
