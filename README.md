# OpenTelemetry Python tests

## Zero-code instrumentation with output to console

```bash
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument \
  --traces_exporter console \
  --metrics_exporter console \
  --logs_exporter console \
  --service_name dice-server \
  flask --app app01-zerocode-instrumentation run -p 8080
```

## Start OpenTelemetry Collector

```bash
docker run -p 4317:4317 \
  -v ./otel-collector-config.yaml:/etc/otel-collector-config.yaml \
  otel/opentelemetry-collector:latest \
  --config=/etc/otel-collector-config.yaml
```
