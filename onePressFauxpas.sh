#!/bin/bash
base_dir=$(cd "$(dirname "$0")";pwd)
file_path=${base_dir}/result2.txt
file_replace_path=${base_dir}/result2_replace.txt
script_path=${base_dir}/filterFauxpas.py
# file=${base_dir}/result2.txt

function check_file {
  #statements
  echo $file_path
  if [ -f "$file_path" ]; then
    # echo "test"
    rm -rf $file_path
  fi

  # echo $file_path
  if [ -f "$file_replace_path" ]; then
    # echo "test"
    rm -rf $file_replace_path
  fi
}

function check_script {
  #statements
  # echo $script_path
  if [ ! -x "$script_path"];then
    chmod a+x $script_path
  fi
}

function update_code {
  #statements
  cd /Users/didi/Desktop/SCar/SCarCore
  git pull
  cd /Users/didi/Desktop/SCar/ONESCar
  git pull
  cd $base_dirSS
}

function check_project {
  #statements
  update_code
  fauxpas check /Users/didi/Desktop/SCar/Pods/Pods.xcodeproj --target SCarCommon >>result2.txt
  # file_path=${base_dir}/result2.txt
  # script_path=${base_dir}/filterFauxpas.py
  # echo $file_path
  if [ -f "$file_path" ]; then
    check_script
    python $script_path
  fi
}



check_file
check_project
check_file
