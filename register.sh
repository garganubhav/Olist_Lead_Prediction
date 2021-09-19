docker build . -t $BUILD_IMAGE_LOCAL
docker tag $BUILD_IMAGE_LOCAL $CI_COMMIT_SHA
docker push anubhavgarg/$CI_COMMIT_SHA
