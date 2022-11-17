# pragmatics-pyro

Port of [www.problang.org](www.problang.org) (problang.org is written in WebPPL, this repository is in [pyro.ai](pyro))

So far Chapters 01 and 09 have been included, with exercises, solutions and slides.

In the notebooks, utterances are interpreted by listeners which model the decisions of a speaker, and in doing so infer the intended meaning as well as properties of the speaker.


![pragmaticlistener](pragmatic_listener.png)

# Example Setup

```
git clone https://www.github.com/marvosyntactical/pragmatics-pyro/
cd pragmatics-pyro
virtualenv myenv
source myenv/bin/activate
python3 setup.py install
python -m ipykernel install --name my_env_name
```

## Example execution
```
jupyter lab course/chapters/
# Then select Kernel->Change Kernel...->my_env_name
```


