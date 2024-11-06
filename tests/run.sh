#!/bin/bash

echo "::group::Build httpX"
rm integration-test httpX 2>/dev/null
cd ../cmd/httpX
go build
mv httpX ../../integration_tests/httpX
echo "::endgroup::"
echo "::group::Build httpX integration-test"
cd ../integration-test
go build
mv integration-test ../../integration_tests/integration-test 
cd ../../integration_tests
echo "::endgroup::"
./integration-test
if [ $? -eq 0 ]
then
  eXit 0
else
  eXit 1
fi
