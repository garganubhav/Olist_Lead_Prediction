docker build . -t $BUILD_IMAGE_LOCAL
docker tag $BUILD_IMAGE_LOCAL $GITHUB_SHA
docker push anubhavgarg/$BUILD_IMAGE_LOCAL:$GITHUB_SHA
