#!/bin/bash

protoc -I=. ./helloworld.proto --js_out=import_style=commonjs,binary:.