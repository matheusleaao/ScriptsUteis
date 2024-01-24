#!/bin/bash

menu() {
    clear
    echo "==============================="
    echo "     Menu de Instalação"
    echo "==============================="
    echo "1. Instalar Docker"
    echo "2. Instalar Git"
    echo "3. Instalar Ansible"
    echo "4. Instalar AWS CLI"
    echo "5. Instalar Python3 e pip"
    echo "6. Instalar Terraform"
    echo "7. Instalar todos os serviços"
    echo "8. Sair"
    echo "==============================="
}

instalar_docker() {
    echo "Instalando Docker..."
}

instalar_git() {
    echo "Instalando Git..."
    sudo apt-get update
    sudo apt-get install -y git
}

instalar_ansible() {
    echo "Instalando Ansible..."
    sudo apt-add-repository ppa:ansible/ansible
    sudo apt install ansible
}

instalar_awscli() {
    echo "Instalando AWS CLI..."
    mkdir awscli
    cd awscli
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install
    cd ..
}

instalar_python_pip() {
    echo "Instalando Python3 e pip..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
}

install_terraform() {
    if [ ! -d "tf_Switch_version-Lion" ]; then
        git clone https://github.com/matheusleaao/tf_Switch_version-Lion.git
    fi

    cd tf_Switch_version-Lion
    sudo ./switch_version.sh
}

instalar_todos() {
    instalar_docker
    instalar_git
    instalar_ansible
    instalar_awscli
    instalar_python_pip
    install_terraform
}

while true; do
    menu
    read -p "Escolha uma opção: " opcao

    case $opcao in
        1) instalar_docker ;;
        2) instalar_git ;;
        3) instalar_ansible ;;
        4) instalar_awscli ;;
        5) instalar_python_pip ;;
        6) install_terraform ;;
        7) instalar_todos ;;
        8) break ;;
        *) echo "Opção inválida. Tente novamente." ;;
    esac

    read -p "Pressione Enter para continuar..."
done

echo "Script encerrado."

