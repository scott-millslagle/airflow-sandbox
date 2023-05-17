FROM gitpod/workspace-full

USER gitpod

RUN bash -c ". .nvm/nvm.sh \
    && nvm install v16 \
    && nvm use v16 \
    && nvm alias default v16"
