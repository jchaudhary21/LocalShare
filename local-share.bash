    local python_file=$(find ~/ -name "/home/jc/Desktop/advanceCopyPaste/local-share-server.py")

    if [ ! -f "$python_file" ]; then
        echo "File '$python_file' does not exist."
        return 1
    fi
    
    python3 "$python_file" >/dev/null 2>&1 &
    
    flask_pid=$!
    
    ip_address=$(hostname -I | awk '{print $1}')
   
    echo -e "Access file from here : \e[1mhttp://$ip_address:5000\e[0m"
    echo -e "\e[41;97mPress CTRL+C to stop\e[0m"  
    trap 'kill $flask_pid >/dev/null 2>&1; echo "Stopped"; exit' SIGINT
    
    while true; do
        wait $flask_pid >/dev/null 2>&1
        if [ $? -eq 0 ]; then
            break
        fi
    done