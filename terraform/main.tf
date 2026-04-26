provider "aws" {
  region = "ap-southeast-1"
}

resource "aws_security_group" "hudafikr_sg" {
  name = "hudafikr-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "hudafikr" {
  ami           = "ami-0df7a207adb9748c7"
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.hudafikr_sg.id]

  key_name = "hudafikr-key"

  tags = {
    Name = "hudafikr-server"
  }
}