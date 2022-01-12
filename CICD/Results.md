#Results of Circle CI

**Spin up environment**
Build-agent version 1.0.100208-e2aaf0f1 (2022-01-11T23:24:42+0000)
System information:
 Server Version: 20.10.11
 Storage Driver: overlay2
  Backing Filesystem: xfs
 Cgroup Driver: cgroupfs
 Cgroup Version: 1
 Kernel Version: 5.11.0-1022-aws
 Operating System: Ubuntu 20.04.3 LTS
 OSType: linux
 Architecture: x86_64

Starting container circleci/python:3.8
circleci/python:3.8:
  using image circleci/python@sha256:51d0b0a859b1268c6ec7e48279cb6d0f7ddffa1676f1dd22cee54214d08cdc44
  pull stats: Image was already available so the image was not pulled
  time to create container: 110ms
Warning: No authentication provided, using CircleCI credentials for pulls from Docker Hub.
  image is cached as circleci/python:3.8, but refreshing...
3.8: Pulling from circleci/python
Digest: sha256:51d0b0a859b1268c6ec7e48279cb6d0f7ddffa1676f1dd22cee54214d08cdc44
Status: Image is up to date for circleci/python:3.8
Time to upload agent and config: 380.900651ms
Time to start containers: 319.90813ms

**Preparing environment variables**
Using build environment variables:
  BASH_ENV=/tmp/.bash_env-61deae47684078714f55eaab-0-build
  CI=true
  CIRCLECI=true
  CIRCLE_BRANCH=master
  CIRCLE_BUILD_NUM=6
  CIRCLE_BUILD_URL=https://circleci.com/gh/SamiNenno/NewsPoll/6
  CIRCLE_COMPARE_URL=
  CIRCLE_JOB=build
  CIRCLE_NODE_INDEX=0
  CIRCLE_NODE_TOTAL=1
  CIRCLE_PREVIOUS_BUILD_NUM=5
  CIRCLE_PROJECT_REPONAME=NewsPoll
  CIRCLE_PROJECT_USERNAME=SamiNenno
  CIRCLE_REPOSITORY_URL=git@github.com:SamiNenno/NewsPoll.git
  CIRCLE_SHA1=95959e3ad242ad3c1a0d5dd90d2c5c356e8c1b8c
  CIRCLE_SHELL_ENV=/tmp/.bash_env-61deae47684078714f55eaab-0-build
  CIRCLE_STAGE=build
  CIRCLE_USERNAME=SamiNenno
  CIRCLE_WORKFLOW_ID=7fa5a52b-803c-432e-ab6d-a54c64eec203
  CIRCLE_WORKFLOW_JOB_ID=5d1ce785-ecde-4770-86b3-a0253f885966
  CIRCLE_WORKFLOW_UPSTREAM_JOB_IDS=
  CIRCLE_WORKFLOW_WORKSPACE_ID=7fa5a52b-803c-432e-ab6d-a54c64eec203
  CIRCLE_WORKING_DIRECTORY=~/repo


The redacted variables listed above will be masked in run step output.

**Checkout Code**
#!/bin/sh
set -e
# Workaround old docker images with incorrect $HOME
# check https://github.com/docker/docker/issues/2968 for details
if [ "${HOME}" = "/" ]
then
  export HOME=$(getent passwd $(id -un) | cut -d: -f6)
fi

echo "Using SSH Config Dir '$SSH_CONFIG_DIR'"
git --version 

mkdir -p "$SSH_CONFIG_DIR"
chmod 0700 "$SSH_CONFIG_DIR"

printf "%s" 'github.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==
github.com ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEmKSENjQEezOmxkZMy7opKgwFB9nkt5YRrYMjNuG5N87uRgg6CLrbo5wAdT/y6v0mKV0U2w0WZ2YB/++Tpockg=
github.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOMqqnkVzrm0SdG6UOoqKLsabgH5C9okWi0dh2l9GKJl
bitbucket.org ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAubiN81eDcafrgMeLzaFPsw2kNvEcqTKl/VqLat/MaB33pZy0y3rJZtnqwR2qOOvbwKZYKiEO1O6VqNEBxKvJJelCq0dTXWT5pbO2gDXC6h6QDXCaHo6pOHGPUy+YBaGQRGuSusMEASYiWunYN0vCAI8QaXnWMXNMdFP3jHAJH0eDsoiGnLPBlBp4TNm6rYI74nMzgz3B9IikW4WVK+dc8KZJZWYjAuORU3jc1c/NPskD2ASinf8v3xnfXeukU0sJ5N6m5E8VLjObPEO+mN2t/FZTMZLiFqPWc/ALSqnMnnhwrNi2rbfg/rd/IpL8Le3pSBne8+seeFVBoGqzHM9yXw==
gitlab.com ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFSMqzJeV9rUzU4kWitGjeR4PWSa29SPqJ1fVkhtj3Hw9xjLVXVYrU9QlYWrOLXBpQ6KWjbjTDTdDkoohFzgbEY=
' >> "$SSH_CONFIG_DIR/known_hosts"
chmod 0600 "$SSH_CONFIG_DIR/known_hosts"

rm -f "$SSH_CONFIG_DIR/id_rsa"
printf "%s" "$CHECKOUT_KEY" > "$SSH_CONFIG_DIR/id_rsa"
chmod 0600 "$SSH_CONFIG_DIR/id_rsa"
if (: "${CHECKOUT_KEY_PUBLIC?}") 2>/dev/null; then
  rm -f "$SSH_CONFIG_DIR/id_rsa.pub"
  printf "%s" "$CHECKOUT_KEY_PUBLIC" > "$SSH_CONFIG_DIR/id_rsa.pub"
fi

export GIT_SSH_COMMAND='ssh -i "$SSH_CONFIG_DIR/id_rsa" -o UserKnownHostsFile="$SSH_CONFIG_DIR/known_hosts"'

# use git+ssh instead of https
git config --global url."ssh://git@github.com".insteadOf "https://github.com" || true
git config --global gc.auto 0 || true

if [ -e '/home/circleci/repo/.git' ] ; then
  echo 'Fetching into existing repository'
  existing_repo='true'
  cd '/home/circleci/repo'
  git remote set-url origin "$CIRCLE_REPOSITORY_URL" || true
else
  echo 'Cloning git repository'
  existing_repo='false'
  mkdir -p '/home/circleci/repo'
  cd '/home/circleci/repo'
  git clone --no-checkout "$CIRCLE_REPOSITORY_URL" .
fi

if [ "$existing_repo" = 'true' ] || [ 'false' = 'true' ]; then
  echo 'Fetching from remote repository'
  if [ -n "$CIRCLE_TAG" ]; then
    git fetch --force --tags origin
  else
    git fetch --force origin +refs/heads/master:refs/remotes/origin/master
  fi
fi

if [ -n "$CIRCLE_TAG" ]; then
  echo 'Checking out tag'
  git checkout --force "$CIRCLE_TAG"
  git reset --hard "$CIRCLE_SHA1"
else
  echo 'Checking out branch'
  git checkout --force -B "$CIRCLE_BRANCH" "$CIRCLE_SHA1"
  git --no-pager log --no-color -n 1 --format='HEAD is now at %h %s'
fi

Using SSH Config Dir '/home/circleci/.ssh'
git version 2.30.2
Cloning git repository
Cloning into '.'...
Warning: Permanently added the ECDSA host key for IP address '140.82.112.3' to the list of known hosts.
remote: Enumerating objects: 224, done.        
remote: Counting objects: 100% (224/224), done.        
remote: Compressing objects: 100% (160/160), done.        
remote: Total 224 (delta 106), reused 168 (delta 50), pack-reused 0        
Receiving objects: 100% (224/224), 2.66 MiB | 5.66 MiB/s, done.
Resolving deltas: 100% (106/106), done.
Checking out branch
Reset branch 'master'
Your branch is up to date with 'origin/master'.
HEAD is now at 95959e3 Small fix on config.yml

**Install dependencies**
#!/bin/bash -eo pipefail
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

Collecting pandas~=1.3.3
  Downloading pandas-1.3.5-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.5 MB)
     |████████████████████████████████| 11.5 MB 27.2 MB/s eta 0:00:011
Collecting plotly~=5.3.1
  Downloading plotly-5.3.1-py2.py3-none-any.whl (23.9 MB)
     |████████████████████████████████| 23.9 MB 97.5 MB/s eta 0:00:0111
Collecting pendulum~=2.1.2
  Downloading pendulum-2.1.2-cp38-cp38-manylinux1_x86_64.whl (155 kB)
     |████████████████████████████████| 155 kB 104.1 MB/s eta 0:00:01
Collecting requests~=2.26.0
  Downloading requests-2.26.0-py2.py3-none-any.whl (62 kB)
     |████████████████████████████████| 62 kB 3.2 MB/s s eta 0:00:01
Collecting numpy~=1.19.5
  Downloading numpy-1.19.5-cp38-cp38-manylinux2010_x86_64.whl (14.9 MB)
     |████████████████████████████████| 14.9 MB 104.3 MB/s eta 0:00:011
Collecting flashtext~=2.7
  Downloading flashtext-2.7.tar.gz (14 kB)
Collecting flake8~=4.0.1
  Downloading flake8-4.0.1-py2.py3-none-any.whl (64 kB)
     |████████████████████████████████| 64 kB 368 kB/s  eta 0:00:01
Collecting pytest~=6.2.5
  Downloading pytest-6.2.5-py3-none-any.whl (280 kB)
     |████████████████████████████████| 280 kB 68.2 MB/s eta 0:00:01
Collecting python-dateutil>=2.7.3
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     |████████████████████████████████| 247 kB 110.6 MB/s eta 0:00:01
Collecting pytz>=2017.3
  Downloading pytz-2021.3-py2.py3-none-any.whl (503 kB)
     |████████████████████████████████| 503 kB 104.0 MB/s eta 0:00:01
Collecting tenacity>=6.2.0
  Downloading tenacity-8.0.1-py3-none-any.whl (24 kB)
Collecting six
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting pytzdata>=2020.1
  Downloading pytzdata-2020.1-py2.py3-none-any.whl (489 kB)
     |████████████████████████████████| 489 kB 110.8 MB/s eta 0:00:01
Collecting charset-normalizer~=2.0.0
  Downloading charset_normalizer-2.0.10-py3-none-any.whl (39 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2021.10.8-py2.py3-none-any.whl (149 kB)
     |████████████████████████████████| 149 kB 112.3 MB/s eta 0:00:01
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.8-py2.py3-none-any.whl (138 kB)
     |████████████████████████████████| 138 kB 70.0 MB/s eta 0:00:0101
Collecting idna<4,>=2.5
  Downloading idna-3.3-py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 29.9 MB/s eta 0:00:01
Collecting pycodestyle<2.9.0,>=2.8.0
  Downloading pycodestyle-2.8.0-py2.py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 5.0 MB/s  eta 0:00:01
Collecting pyflakes<2.5.0,>=2.4.0
  Downloading pyflakes-2.4.0-py2.py3-none-any.whl (69 kB)
     |████████████████████████████████| 69 kB 23.3 MB/s eta 0:00:01
Collecting mccabe<0.7.0,>=0.6.0
  Downloading mccabe-0.6.1-py2.py3-none-any.whl (8.6 kB)
Collecting toml
  Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Collecting packaging
  Downloading packaging-21.3-py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 24.7 MB/s eta 0:00:01
Collecting pluggy<2.0,>=0.12
  Downloading pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
Collecting py>=1.8.2
  Downloading py-1.11.0-py2.py3-none-any.whl (98 kB)
     |████████████████████████████████| 98 kB 32.7 MB/s  eta 0:00:01
Collecting iniconfig
  Downloading iniconfig-1.1.1-py2.py3-none-any.whl (5.0 kB)
Collecting attrs>=19.2.0
  Downloading attrs-21.4.0-py2.py3-none-any.whl (60 kB)
     |████████████████████████████████| 60 kB 31.2 MB/s eta 0:00:01
Collecting pyparsing!=3.0.5,>=2.0.2
  Downloading pyparsing-3.0.6-py3-none-any.whl (97 kB)
     |████████████████████████████████| 97 kB 23.4 MB/s  eta 0:00:01
Using legacy 'setup.py install' for flashtext, since package 'wheel' is not installed.
Installing collected packages: six, pyparsing, urllib3, toml, tenacity, pytzdata, pytz, python-dateutil, pyflakes, pycodestyle, py, pluggy, packaging, numpy, mccabe, iniconfig, idna, charset-normalizer, certifi, attrs, requests, pytest, plotly, pendulum, pandas, flashtext, flake8
    Running setup.py install for flashtext ... - done
Successfully installed attrs-21.4.0 certifi-2021.10.8 charset-normalizer-2.0.10 flake8-4.0.1 flashtext-2.7 idna-3.3 iniconfig-1.1.1 mccabe-0.6.1 numpy-1.19.5 packaging-21.3 pandas-1.3.5 pendulum-2.1.2 plotly-5.3.1 pluggy-1.0.0 py-1.11.0 pycodestyle-2.8.0 pyflakes-2.4.0 pyparsing-3.0.6 pytest-6.2.5 python-dateutil-2.8.2 pytz-2021.3 pytzdata-2020.1 requests-2.26.0 six-1.16.0 tenacity-8.0.1 toml-0.10.2 urllib3-1.26.8
WARNING: You are using pip version 21.1.1; however, version 21.3.1 is available.
You should consider upgrading via the '/home/circleci/repo/venv/bin/python3 -m pip install --upgrade pip' command.
CircleCI received exit code 0

**Run tests**
#!/bin/bash -eo pipefail
. venv/bin/activate
flake8 --exclude=venv* --statistics
pytest Preprocess.py
pytest Newscounter.py
pytest Visuals.py

./Newscounter.py:15:80: E501 line too long (83 > 79 characters)
./Newscounter.py:34:80: E501 line too long (94 > 79 characters)
./Newscounter.py:35:80: E501 line too long (87 > 79 characters)
./Newscounter.py:37:80: E501 line too long (85 > 79 characters)
./Newscounter.py:44:80: E501 line too long (109 > 79 characters)
./Newscounter.py:49:80: E501 line too long (128 > 79 characters)
./Newscounter.py:56:5: E303 too many blank lines (2)
./Newscounter.py:57:80: E501 line too long (94 > 79 characters)
./Newscounter.py:60:80: E501 line too long (96 > 79 characters)
./Newscounter.py:62:59: E231 missing whitespace after ','
./Newscounter.py:62:80: E501 line too long (92 > 79 characters)
./Newscounter.py:63:60: E231 missing whitespace after ','
./Newscounter.py:63:80: E501 line too long (133 > 79 characters)
./Newscounter.py:64:80: E501 line too long (90 > 79 characters)
./Newscounter.py:68:80: E501 line too long (92 > 79 characters)
./Newscounter.py:71:80: E501 line too long (93 > 79 characters)
./Newscounter.py:105:80: E501 line too long (105 > 79 characters)
./Newscounter.py:106:80: E501 line too long (93 > 79 characters)
./Newscounter.py:108:45: E231 missing whitespace after ':'
./Newscounter.py:109:80: E501 line too long (88 > 79 characters)
./Newscounter.py:113:17: E128 continuation line under-indented for visual indent
./Newscounter.py:113:80: E501 line too long (116 > 79 characters)
./Newsfeeler.py:1:1: F401 'os' imported but unused
./Newsfeeler.py:2:1: F401 'pandas as pd' imported but unused
./Preprocess.py:9:1: E302 expected 2 blank lines, found 1
./Preprocess.py:14:80: E501 line too long (89 > 79 characters)
./Preprocess.py:17:5: E266 too many leading '#' for block comment
./Preprocess.py:18:31: E251 unexpected spaces around keyword / parameter equals
./Preprocess.py:18:33: E251 unexpected spaces around keyword / parameter equals
./Preprocess.py:22:49: E225 missing whitespace around operator
./Preprocess.py:48:9: E266 too many leading '#' for block comment
./Preprocess.py:48:80: E501 line too long (80 > 79 characters)
./Preprocess.py:49:9: E266 too many leading '#' for block comment
./Preprocess.py:49:80: E501 line too long (116 > 79 characters)
./Preprocess.py:52:9: E266 too many leading '#' for block comment
./Preprocess.py:53:9: E266 too many leading '#' for block comment
./Preprocess.py:56:9: E266 too many leading '#' for block comment
./Preprocess.py:57:9: E266 too many leading '#' for block comment
./Preprocess.py:57:80: E501 line too long (90 > 79 characters)
./Preprocess.py:60:9: E266 too many leading '#' for block comment
./Preprocess.py:61:9: E266 too many leading '#' for block comment
./Preprocess.py:63:80: E501 line too long (82 > 79 characters)
./Preprocess.py:68:80: E501 line too long (82 > 79 characters)
./Preprocess.py:94:80: E501 line too long (93 > 79 characters)
./Preprocess.py:95:80: E501 line too long (90 > 79 characters)
./Preprocess.py:102:80: E501 line too long (87 > 79 characters)
./Preprocess.py:110:80: E501 line too long (81 > 79 characters)
./Preprocess.py:122:80: E501 line too long (81 > 79 characters)
./Preprocess.py:126:80: E501 line too long (85 > 79 characters)
./Preprocess.py:140:80: E501 line too long (100 > 79 characters)
./Preprocess.py:142:80: E501 line too long (87 > 79 characters)
./Preprocess.py:143:80: E501 line too long (149 > 79 characters)
./Preprocess.py:144:80: E501 line too long (146 > 79 characters)
./Preprocess.py:145:80: E501 line too long (86 > 79 characters)
./Preprocess.py:156:80: E501 line too long (85 > 79 characters)
./Preprocess.py:158:1: E302 expected 2 blank lines, found 1
./Preprocess.py:166:49: E225 missing whitespace around operator
./Preprocess.py:167:80: E501 line too long (81 > 79 characters)
./Preprocess.py:170:37: E231 missing whitespace after ':'
./Preprocess.py:170:47: E231 missing whitespace after ':'
./Preprocess.py:170:59: E231 missing whitespace after ':'
./Preprocess.py:170:69: E231 missing whitespace after ':'
./Preprocess.py:170:80: E501 line too long (94 > 79 characters)
./Preprocess.py:170:81: E231 missing whitespace after ':'
./Preprocess.py:170:91: E231 missing whitespace after ':'
./Preprocess.py:176:80: E501 line too long (95 > 79 characters)
./Preprocess.py:191:80: E501 line too long (84 > 79 characters)
./Preprocess.py:197:80: E501 line too long (83 > 79 characters)
./Preprocess.py:199:80: E501 line too long (106 > 79 characters)
./Preprocess.py:211:5: E303 too many blank lines (2)
./Preprocess.py:220:80: E501 line too long (91 > 79 characters)
./Preprocess.py:240:49: E225 missing whitespace around operator
./Preprocess.py:241:9: E266 too many leading '#' for block comment
./Preprocess.py:242:9: E266 too many leading '#' for block comment
./Preprocess.py:243:80: E501 line too long (90 > 79 characters)
./Preprocess.py:245:80: E501 line too long (98 > 79 characters)
./Preprocess.py:254:80: E501 line too long (100 > 79 characters)
./Preprocess.py:263:80: E501 line too long (122 > 79 characters)
./Preprocess.py:266:80: E501 line too long (94 > 79 characters)
./Preprocess.py:271:48: E231 missing whitespace after ','
./Preprocess.py:273:48: E231 missing whitespace after ','
./Preprocess.py:281:80: E501 line too long (103 > 79 characters)
./Preprocess.py:283:69: E712 comparison to True should be 'if cond is True:' or 'if cond:'
./Preprocess.py:283:80: E501 line too long (84 > 79 characters)
./Preprocess.py:295:1: E302 expected 2 blank lines, found 1
./Preprocess.py:304:80: E501 line too long (82 > 79 characters)
./Preprocess.py:306:80: E501 line too long (123 > 79 characters)
./Preprocess.py:313:80: E501 line too long (114 > 79 characters)
./Preprocess.py:330:80: E501 line too long (92 > 79 characters)
./Preprocess.py:332:80: E501 line too long (97 > 79 characters)
./Preprocess.py:356:1: W391 blank line at end of file
./Visuals.py:7:1: E302 expected 2 blank lines, found 1
./Visuals.py:10:80: E501 line too long (100 > 79 characters)
./Visuals.py:11:80: E501 line too long (88 > 79 characters)
./Visuals.py:12:80: E501 line too long (88 > 79 characters)
./Visuals.py:41:41: E231 missing whitespace after ':'
./Visuals.py:41:56: E231 missing whitespace after ':'
./Visuals.py:47:80: E501 line too long (83 > 79 characters)
./Visuals.py:49:80: E501 line too long (82 > 79 characters)
./Visuals.py:67:35: E231 missing whitespace after ':'
./Visuals.py:69:80: E501 line too long (83 > 79 characters)
./Visuals.py:71:80: E501 line too long (82 > 79 characters)
./Visuals.py:76:80: E501 line too long (98 > 79 characters)
./Visuals.py:92:59: E231 missing whitespace after ','
./Visuals.py:92:65: E231 missing whitespace after ','
./Visuals.py:92:73: E231 missing whitespace after ','
./Visuals.py:92:80: E501 line too long (105 > 79 characters)
./Visuals.py:92:81: E231 missing whitespace after ','
./Visuals.py:92:87: E231 missing whitespace after ','
./Visuals.py:92:93: E231 missing whitespace after ','
./Visuals.py:93:80: E501 line too long (106 > 79 characters)
./Visuals.py:117:29: E251 unexpected spaces around keyword / parameter equals
./Visuals.py:117:31: E251 unexpected spaces around keyword / parameter equals
./Visuals.py:123:29: E251 unexpected spaces around keyword / parameter equals
./Visuals.py:123:31: E251 unexpected spaces around keyword / parameter equals
./Visuals.py:124:29: E203 whitespace before ':'
./Visuals.py:132:80: E501 line too long (89 > 79 characters)
./Visuals.py:143:50: E231 missing whitespace after ':'
./Visuals.py:143:61: E231 missing whitespace after ':'
./Visuals.py:146:28: E231 missing whitespace after ':'
./Visuals.py:146:43: E231 missing whitespace after ':'
./Visuals.py:146:58: E231 missing whitespace after ':'
./Visuals.py:146:75: E231 missing whitespace after ':'
./Visuals.py:146:80: E501 line too long (112 > 79 characters)
./Visuals.py:146:89: E231 missing whitespace after ':'
./Visuals.py:146:105: E231 missing whitespace after ':'
./Visuals.py:167:1: E305 expected 2 blank lines after class or function definition, found 1
./Visuals.py:169:5: E265 block comment should start with '# '
./Visuals.py:170:5: E265 block comment should start with '# '
./Visuals.py:171:5: E265 block comment should start with '# '
./Visuals.py:172:5: E265 block comment should start with '# '
./Visuals.py:173:5: E265 block comment should start with '# '
./Visuals.py:175:5: E265 block comment should start with '# '
./Visuals.py:176:5: E265 block comment should start with '# '
./Visuals.py:177:5: E265 block comment should start with '# '
./Visuals.py:178:5: E265 block comment should start with '# '
./Visuals.py:178:16: W292 no newline at end of file
./Visuals.py:178:16: W292 no newline at end of file
./Visuals.py:178:16: W292 no newline at end of file
./Unittest_Scripts/test_Preprocess.py:4:1: E302 expected 2 blank lines, found 1
./Unittest_Scripts/test_Preprocess.py:7:39: E251 unexpected spaces around keyword / parameter equals
./Unittest_Scripts/test_Preprocess.py:7:80: E501 line too long (93 > 79 characters)
./Unittest_Scripts/test_Preprocess.py:9:9: E266 too many leading '#' for block comment
./Unittest_Scripts/test_Preprocess.py:13:9: E266 too many leading '#' for block comment
./Unittest_Scripts/test_Preprocess.py:20:80: E501 line too long (81 > 79 characters)
./Unittest_Scripts/test_Preprocess.py:25:80: E501 line too long (83 > 79 characters)
./Unittest_Scripts/test_Preprocess.py:27:9: E266 too many leading '#' for block comment
./Unittest_Scripts/test_Preprocess.py:27:80: E501 line too long (95 > 79 characters)
./Unittest_Scripts/test_Preprocess.py:31:80: E501 line too long (84 > 79 characters)
./Unittest_Scripts/test_Preprocess.py:33:9: E266 too many leading '#' for block comment
./Unittest_Scripts/test_Preprocess.py:36:1: E305 expected 2 blank lines after class or function definition, found 1
1     E128 continuation line under-indented for visual indent
1     E203 whitespace before ':'
3     E225 missing whitespace around operator
28    E231 missing whitespace after ','
7     E251 unexpected spaces around keyword / parameter equals
9     E265 block comment should start with '# '
15    E266 too many leading '#' for block comment
5     E302 expected 2 blank lines, found 1
2     E303 too many blank lines (2)
2     E305 expected 2 blank lines after class or function definition, found 1
71    E501 line too long (83 > 79 characters)
1     E712 comparison to True should be 'if cond is True:' or 'if cond:'
2     F401 'os' imported but unused
3     W292 no newline at end of file
1     W391 blank line at end of file

Exited with code exit status 1
CircleCI received exit code 1