job "hello-devops" {
  datacenters = ["dc1"]
  type = "service"

  group "web" {
    count = 1

    task "hello" {
      driver = "docker"

      config {
        image = "devops-intern-hello:latest"
      }

      resources {
        cpu    = 100
        memory = 128
      }
    }
  }
}
