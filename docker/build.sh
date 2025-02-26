#!/bin/bash

echo "Construyendo imagen de preprocesamiento..."
docker build -t ml-price-prep:latest -f docker/Dockerfile.prep .

echo "Construyendo imagen de entrenamiento..."
docker build -t ml-price-train:latest -f docker/Dockerfile.train .

echo "Construyendo imagen de inferencia..."
docker build -t ml-price-inference:latest -f docker/Dockerfile.inference .

echo "¡Construcción completada!" 