docker build . -t $BUILD_IMAGE_LOCAL
export AWS_ECR="075156609000.dkr.ecr.us-west-2.amazonaws.com/dsi-mlops"
docker tag $BUILD_IMAGE_LOCAL $AWS_ECR:$CI_COMMIT_SHA
docker push $AWS_ECR:$CI_COMMIT_SHA
