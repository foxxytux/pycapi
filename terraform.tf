terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "ssh://user@SERVER_IP"
}

resource "docker_network" "app_network" {
  name = "pycapi_prod_network"
}

resource "docker_volume" "db_volume" {
  name = "pycapi_data"
}
