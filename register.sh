docker build . -t $BUILD_IMAGE_LOCAL
docker tag $BUILD_IMAGE_LOCAL olist:$GITHUB_SHA
docker push anubhavgarg/olist:$GITHUB_SHA
