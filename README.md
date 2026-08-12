Awesome Precipitation Nowcasting (Redux)
==

👋 Hello! Welcome to a collection of papers, datasets, and other resources related to the (longstanding, but particuarly relevant) task of *precipitation nowcasting*—which we will define as "predicting future precipitation rates or observations (e.g., radar reflectivity) with **0-6 hour** lead times and **sub-hourly temporal resolution** (excluding CAM emulators etc)." 

<p align="center">
  <img src="assets/IMERG_GrandAvg_2024_Colorbar.png" alt="Global map of average annual precipitation from GPM IMERG, in mm/year" width="100%">
</p>

* Image credit: NASA Goddard Space Flight Center/[GPM IMERG](https://gpm.nasa.gov/data/imerg).

### TOC
* [:page_facing_up: Papers](https://github.com/tyui592/awesome-precipitation-nowcasting#page_facing_up-papers)
* [:card_file_box: Datasets](https://github.com/tyui592/awesome-precipitation-nowcasting#card_file_box-datasets)
* [:calendar: Workshops](https://github.com/tyui592/awesome-precipitation-nowcasting#calendar-workshops)
* [:package: Libraries](https://github.com/tyui592/awesome-precipitation-nowcasting#package-libraries)
<!-- * [:link: Others](https://github.com/tyui592/awesome-precipitation-nowcasting#link-others) -->
<!-- *If I missed any of your work, or if something here needs an update, please email me or just open a pull request. Thank you!* -->

:page_facing_up: Papers
==

## Modern era (~2000-2015)

##### (2003) Distributed Quantitative Precipitation Forecasting Using Information from Radar and Numerical Weather Prediction Models
* Venue: *Journal of Hydrometeorology*
* Model: DQPF
<details><summary>bibtex</summary>

```bibtex
@article{ganguly2003distributed,
  author = {Ganguly, Auroop R. and Bras, Rafael L.},
  title = {Distributed Quantitative Precipitation Forecasting Using Information from Radar and Numerical Weather Prediction Models},
  journal = {Journal of Hydrometeorology},
  volume = {4},
  number = {6},
  pages = {1168--1180},
  year = {2003},
  doi = {10.1175/1525-7541(2003)004<1168:DQPFUI>2.0.CO;2}
}
```

</details>

## Machine learning era (~2015-present)

### Google/DeepMind <img src="https://www.google.com/s2/favicons?domain=google.com&sz=64" height="40" align="center" alt="Google logo">
---

##### (2019) Machine Learning for Precipitation Nowcasting from Radar Images
* Venue: *arXiv*
* Blog: https://ai.googleblog.com/2020/01/using-machine-learning-to-nowcast.html
<details><summary>bibtex</summary>

```bibtex
@misc{agrawal2019machine,
  author = {Shreya Agrawal and Luke Barrington and Carla Bromberg and John Burge and Cenk Gazen and Jason Hickey},
  title = {Machine Learning for Precipitation Nowcasting from Radar Images},
  year = {2019},
  eprint = {1912.12132},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV}
}
```

</details>

##### (2020) MetNet: A Neural Weather Model for Precipitation Forecasting
* Venue: *arXiv*
* Model: MetNet
* GitHub: https://github.com/openclimatefix/metnet
<details><summary>bibtex</summary>

```bibtex
@misc{sonderby2020metnet,
  author = {Casper Kaae Sønderby and Lasse Espeholt and Jonathan Heek and Mostafa Dehghani and Avital Oliver and Tim Salimans and Shreya Agrawal and Jason Hickey and Nal Kalchbrenner},
  title = {MetNet: A Neural Weather Model for Precipitation Forecasting},
  year = {2020},
  eprint = {2003.12140},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG}
}
```

</details>

##### (2021) Skilful precipitation nowcasting using deep generative models of radar
* Venue: *Nature*
* Model: DGMR
* GitHub: https://github.com/deepmind/deepmind-research/tree/master/nowcasting, https://github.com/openclimatefix/skillful_nowcasting
<details><summary>bibtex</summary>

```bibtex
@article{ravuri2021skilful,
  author = {Ravuri, Suman and Lenc, Karel and Willson, Matthew and Kangin, Dmitry and Lam, Remi and Mirowski, Piotr and Fitzsimons, Megan and Athanassiadou, Maria and Kashem, Sheleem and Madge, Sam and Prudden, Rachel and Mandhane, Amol and Clark, Aidan and Brock, Andrew and Simonyan, Karen and Hadsell, Raia and Robinson, Niall and Clancy, Ellen and Arribas, Alberto and Mohamed, Shakir},
  title = {Skilful precipitation nowcasting using deep generative models of radar},
  journal = {Nature},
  volume = {597},
  number = {7878},
  pages = {672--677},
  year = {2021},
  doi = {10.1038/s41586-021-03854-z}
}
```

</details>

##### (2021) Skillful Twelve Hour Precipitation Forecasts using Large Context Neural Networks
* Venue: *arXiv*
* Model: MetNet-2
* Journal version: Deep learning for twelve hour precipitation forecasts (*Nature Communications*, 2022)
* Blog: https://ai.googleblog.com/2021/11/metnet-2-deep-learning-for-12-hour.html
<details><summary>bibtex</summary>

```bibtex
@misc{espeholt2021skillful,
  author = {Lasse Espeholt and Shreya Agrawal and Casper Sønderby and Manoj Kumar and Jonathan Heek and Carla Bromberg and Cenk Gazen and Jason Hickey and Aaron Bell and Nal Kalchbrenner},
  title = {Skillful Twelve Hour Precipitation Forecasts using Large Context Neural Networks},
  year = {2021},
  eprint = {2111.07470},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG}
}

@article{espeholt2022deep,
  author = {Espeholt, Lasse and Agrawal, Shreya and Sønderby, Casper and Kumar, Manoj and Heek, Jonathan and Bromberg, Carla and Gazen, Cenk and Carver, Rob and Andrychowicz, Marcin and Hickey, Jason and Bell, Aaron and Kalchbrenner, Nal},
  title = {Deep learning for twelve hour precipitation forecasts},
  journal = {Nature Communications},
  volume = {13},
  number = {1},
  year = {2022},
  doi = {10.1038/s41467-022-32483-x}
}
```

</details>

##### (2023) Deep Learning for Day Forecasts from Sparse Observations
* Venue: *arXiv*
* Model: MetNet-3
* GitHub: https://github.com/lucidrains/metnet3-pytorch
* Blog: https://research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/
<details><summary>bibtex</summary>

```bibtex
@misc{andrychowicz2023deep,
  author = {Marcin Andrychowicz and Lasse Espeholt and Di Li and Samier Merchant and Alexander Merose and Fred Zyda and Shreya Agrawal and Nal Kalchbrenner},
  title = {Deep Learning for Day Forecasts from Sparse Observations},
  year = {2023},
  eprint = {2306.06079},
  archivePrefix = {arXiv},
  primaryClass = {physics.ao-ph}
}
```

</details>

##### (2023) Learning skillful medium-range global weather forecasting
* Venue: *Science*
* Model: GraphCast
* GitHub: https://github.com/google-deepmind/graphcast
<details><summary>bibtex</summary>

```bibtex
@article{lam2023graphcast,
  author = {Lam, Remi and Sanchez-Gonzalez, Alvaro and Willson, Matthew and Wirnsberger, Peter and Fortunato, Meire and Alet, Ferran and Ravuri, Suman and Ewalds, Timo and Eaton-Rosen, Zach and Hu, Weihua and Merose, Alexander and Hoyer, Stephan and Holland, George and Vinyals, Oriol and Stott, Jacklynn and Pritzel, Alexander and Mohamed, Shakir and Battaglia, Peter},
  title = {Learning skillful medium-range global weather forecasting},
  journal = {Science},
  volume = {382},
  number = {6677},
  pages = {1416--1421},
  year = {2023},
  doi = {10.1126/science.adi2336}
}
```

</details>

### NVIDIA <img src="https://www.google.com/s2/favicons?domain=nvidia.com&sz=64" height="40" align="center" alt="NVIDIA logo">
---

##### (2026) Learning Accurate Storm-Scale Evolution from Observations
* Venue: *arXiv*
* Model: Stormscope
<details><summary>bibtex</summary>

```bibtex
@misc{pathak2026stormscope,
  author = {Jaideep Pathak and Mohammad Shoaib Abbas and Peter Harrington and Zeyuan Hu and Noah Brenowitz and Suman Ravuri and Alberto Carpentieri and Jussi Leinonen and Corey Adams and Oliver Hennigh and Nicholas Geneva and Dale Durran and Mike Pritchard},
  title = {Learning Accurate Storm-Scale Evolution from Observations},
  year = {2026},
  eprint = {2601.17268},
  archivePrefix = {arXiv},
  primaryClass = {physics.ao-ph}
}
```

</details>

##### (2026) Scaling Storm-Resolving Atmospheric AI Simulation to the Entire Planet
* Venue: *arXiv*
* Model: STRATA
<details><summary>bibtex</summary>

```bibtex
@misc{hu2026strata,
  author = {Zeyuan Hu and Akshay Subramaniam and Noel Keen and Tao Ge and Jaideep Pathak and Mohammad Shoaib Abbas and Suman Ravuri and Karthik Kashinath and Naser Mahfouz and Peter Caldwell and Mike Pritchard and Noah Brenowitz},
  title = {Scaling Storm-Resolving Atmospheric AI Simulation to the Entire Planet},
  year = {2026},
  eprint = {2606.31248},
  archivePrefix = {arXiv},
  primaryClass = {physics.ao-ph}
}
```

</details>

### Others
---

##### (2015) Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting
* Venue: *NeurIPS*
* Model: ConvLSTM
<details><summary>bibtex</summary>

```bibtex
@inproceedings{shi2015convlstm,
  author = {Xingjian Shi and Zhourong Chen and Hao Wang and Dit{-}Yan Yeung and Wai{-}Kin Wong and Wang{-}chun Woo},
  title = {Convolutional {LSTM} Network: {A} Machine Learning Approach for Precipitation Nowcasting},
  booktitle = {Advances in Neural Information Processing Systems 28: Annual Conference on Neural Information Processing Systems 2015, December 7-12, 2015, Montreal, Quebec, Canada},
  pages = {802--810},
  year = {2015},
  url = {https://proceedings.neurips.cc/paper/2015/hash/07563a3fe3bbe7e3ba84431ad9d055af-Abstract.html}
}
```

</details>

##### (2016) Rainfall Prediction: A Deep Learning Approach
* Venue: *Hybrid Artificial Intelligent Systems (HAIS)*
* Model: MLP-based Method
<details><summary>bibtex</summary>

```bibtex
@inbook{hernandez2016rainfall,
  author = {Hernández, Emilcy and Sanchez-Anguix, Victor and Julian, Vicente and Palanca, Javier and Duque, Néstor},
  title = {Rainfall Prediction: A Deep Learning Approach},
  booktitle = {Hybrid Artificial Intelligent Systems},
  publisher = {Springer International Publishing},
  pages = {151--162},
  year = {2016},
  doi = {10.1007/978-3-319-32034-2_13}
}
```

</details>

##### (2017) Deep Learning for Precipitation Nowcasting: A Benchmark and A New Model
* Venue: *NeurIPS*
* Model: TrajGRU
* GitHub: https://github.com/sxjscience/HKO-7
<details><summary>bibtex</summary>

```bibtex
@inproceedings{shi2017trajgru,
  author = {Xingjian Shi and Zhihan Gao and Leonard Lausen and Hao Wang and Dit{-}Yan Yeung and Wai{-}Kin Wong and Wang{-}chun Woo},
  title = {Deep Learning for Precipitation Nowcasting: {A} Benchmark and {A} New Model},
  booktitle = {Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems 2017, December 4-9, 2017, Long Beach, CA, {USA}},
  pages = {5617--5627},
  year = {2017},
  url = {https://proceedings.neurips.cc/paper/2017/hash/a6db4ed04f1621a119799fd3d7545d3d-Abstract.html}
}
```

</details>

##### (2017) A short-term rainfall prediction model using multi-task convolutional neural networks
* Venue: *IEEE ICDM*
* Model: CNN-based Method
<details><summary>bibtex</summary>

```bibtex
@inproceedings{qiu2017shortterm,
  author = {Minghui Qiu and Peilin Zhao and Ke Zhang and Jun Huang and Xing Shi and Xiaoguang Wang and Wei Chu},
  title = {A Short-Term Rainfall Prediction Model Using Multi-task Convolutional Neural Networks},
  booktitle = {2017 {IEEE} International Conference on Data Mining, {ICDM} 2017, New Orleans, LA, USA, November 18-21, 2017},
  pages = {395--404},
  publisher = {{IEEE} Computer Society},
  year = {2017},
  doi = {10.1109/ICDM.2017.49}
}
```

</details>

##### (2019) All convolutional neural networks for radar-based precipitation nowcasting
* Venue: *Procedia Computer Science*
* Model: DozhdyaNet
<details><summary>bibtex</summary>

```bibtex
@article{ayzel2019dozhdyanet,
  author = {Ayzel, G. and Heistermann, M. and Sorokin, A. and Nikitin, O. and Lukyanova, O.},
  title = {All convolutional neural networks for radar-based precipitation nowcasting},
  journal = {Procedia Computer Science},
  volume = {150},
  pages = {186--192},
  year = {2019},
  doi = {10.1016/j.procs.2019.02.036}
}
```

</details>

##### (2019) Optical flow models as an open benchmark for radar-based precipitation nowcasting (rainymotion v0.1)
* Venue: *Geoscientific Model Development*
* Model: rainymotion
* GitHub: https://github.com/hydrogo/rainymotion
<details><summary>bibtex</summary>

```bibtex
@article{ayzel2019rainymotion,
  author = {Ayzel, Georgy and Heistermann, Maik and Winterrath, Tanja},
  title = {Optical flow models as an open benchmark for radar-based precipitation nowcasting (rainymotion v0.1)},
  journal = {Geoscientific Model Development},
  volume = {12},
  number = {4},
  pages = {1387--1402},
  year = {2019},
  doi = {10.5194/gmd-12-1387-2019}
}
```

</details>

##### (2019) Pysteps: an open-source Python library for probabilistic precipitation nowcasting (v1.0)
* Venue: *Geoscientific Model Development*
* Model: pySTEPS
* GitHub: https://github.com/pySTEPS/pysteps
<details><summary>bibtex</summary>

```bibtex
@article{pulkkinen2019pysteps,
  author = {Pulkkinen, Seppo and Nerini, Daniele and Pérez Hortal, Andrés A. and Velasco-Forero, Carlos and Seed, Alan and Germann, Urs and Foresti, Loris},
  title = {Pysteps: an open-source Python library for probabilistic precipitation nowcasting (v1.0)},
  journal = {Geoscientific Model Development},
  volume = {12},
  number = {10},
  pages = {4185--4219},
  year = {2019},
  doi = {10.5194/gmd-12-4185-2019}
}
```

</details>

##### (2020) RainNet v1.0: a convolutional neural network for radar-based precipitation nowcasting
* Venue: *Geoscientific Model Development*
* Model: RainNet
* GitHub: https://github.com/hydrogo/rainnet
<details><summary>bibtex</summary>

```bibtex
@article{ayzel2020rainnet,
  author = {Ayzel, Georgy and Scheffer, Tobias and Heistermann, Maik},
  title = {RainNet v1.0: a convolutional neural network for radar-based precipitation nowcasting},
  journal = {Geoscientific Model Development},
  volume = {13},
  number = {6},
  pages = {2631--2644},
  year = {2020},
  doi = {10.5194/gmd-13-2631-2020}
}
```

</details>

##### (2022) Effective Training Strategies for Deep-learning-based Precipitation Nowcasting and Estimation
* Venue: *Computers & Geosciences*
* Model: DeepRaNE
* GitHub: https://github.com/jihoonko/DeepRaNE
<details><summary>bibtex</summary>

```bibtex
@article{ko2022effective,
  author = {Ko, Jihoon and Lee, Kyuhan and Hwang, Hyunjin and Oh, Seok-Geun and Son, Seok-Woo and Shin, Kijung},
  title = {Effective training strategies for deep-learning-based precipitation nowcasting and estimation},
  journal = {Computers \& Geosciences},
  volume = {161},
  pages = {105072},
  year = {2022},
  doi = {10.1016/j.cageo.2022.105072}
}
```

</details>

##### (2022) Deep-Learning-Based Precipitation Nowcasting with Ground Weather Station Data and Radar Data
* Venue: *arXiv*
* Model: ASOC
<details><summary>bibtex</summary>

```bibtex
@misc{ko2022deep,
  author = {Jihoon Ko and Kyuhan Lee and Hyunjin Hwang and Kijung Shin},
  title = {Deep-Learning-Based Precipitation Nowcasting with Ground Weather Station Data and Radar Data},
  year = {2022},
  eprint = {2210.12853},
  archivePrefix = {arXiv},
  primaryClass = {physics.ao-ph}
}
```

</details>

##### (2022) Earthformer: Exploring Space-Time Transformers for Earth System Forecasting
* Venue: *NeurIPS*
* Model: Earthformer
* GitHub: https://github.com/amazon-science/earth-forecasting-transformer
<details><summary>bibtex</summary>

```bibtex
@inproceedings{gao2022earthformer,
  author = {Zhihan Gao and Xingjian Shi and Hao Wang and Yi Zhu and Yuyang Wang and Mu Li and Dit{-}Yan Yeung},
  title = {Earthformer: Exploring Space-Time Transformers for Earth System Forecasting},
  booktitle = {Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022},
  year = {2022},
  url = {http://papers.nips.cc/paper\_files/paper/2022/hash/a2affd71d15e8fedffe18d0219f4837a-Abstract-Conference.html}
}
```

</details>

##### (2023) Precipitation nowcasting using ground radar data and simpler yet better video prediction deep learning
* Venue: *GIScience & Remote Sensing*
* Model: SimVP
<details><summary>bibtex</summary>

```bibtex
@article{han2023precipitation,
  author = {Han, Daehyeon and Choo, Minki and Im, Jungho and Shin, Yeji and Lee, Juhyun and Jung, Sihun},
  title = {Precipitation nowcasting using ground radar data and simpler yet better video prediction deep learning},
  journal = {GIScience \& Remote Sensing},
  volume = {60},
  number = {1},
  year = {2023},
  doi = {10.1080/15481603.2023.2203363}
}
```

</details>

##### (2023) MM-RNN: A Multimodal RNN for Precipitation Nowcasting
* Venue: *IEEE TGRS*
* Model: MM-RNN
<details><summary>bibtex</summary>

```bibtex
@article{ma2023mmrnn,
  author = {Zhifeng Ma and Hao Zhang and Jie Liu},
  title = {{MM-RNN:} {A} Multimodal {RNN} for Precipitation Nowcasting},
  journal = {{IEEE} Trans. Geosci. Remote. Sens.},
  volume = {61},
  pages = {1--14},
  year = {2023},
  doi = {10.1109/TGRS.2023.3264545}
}
```

</details>

##### (2023) ClimaX: A foundation model for weather and climate
* Venue: *ICML*
* Model: ClimaX
* GitHub: https://github.com/microsoft/ClimaX
* Blog: https://www.microsoft.com/en-us/research/group/autonomous-systems-group-robotics/articles/introducing-climax-the-first-foundation-model-for-weather-and-climate/
<details><summary>bibtex</summary>

```bibtex
@inproceedings{nguyen2023climax,
  author = {Tung Nguyen and Johannes Brandstetter and Ashish Kapoor and Jayesh K. Gupta and Aditya Grover},
  title = {ClimaX: {A} foundation model for weather and climate},
  booktitle = {International Conference on Machine Learning, {ICML} 2023, 23-29 July 2023, Honolulu, Hawaii, {USA}},
  series = {Proceedings of Machine Learning Research},
  volume = {202},
  pages = {25904--25938},
  publisher = {{PMLR}},
  year = {2023},
  url = {https://proceedings.mlr.press/v202/nguyen23a.html}
}
```

</details>

##### (2023) Skilful nowcasting of extreme precipitation with NowcastNet
* Venue: *Nature*
* Model: NowcastNet
<details><summary>bibtex</summary>

```bibtex
@article{zhang2023nowcastnet,
  author = {Zhang, Yuchen and Long, Mingsheng and Chen, Kaiyuan and Xing, Lanxiang and Jin, Ronghua and Jordan, Michael I. and Wang, Jianmin},
  title = {Skilful nowcasting of extreme precipitation with NowcastNet},
  journal = {Nature},
  volume = {619},
  number = {7970},
  pages = {526--532},
  year = {2023},
  doi = {10.1038/s41586-023-06184-4}
}
```

</details>

##### (2023) Deep Learning Model based on Multi-scale Feature Fusion for Precipitation Nowcasting
* Venue: *Geoscientific Model Development (preprint)*
* Model: MFF
<details><summary>bibtex</summary>

```bibtex
@article{tan2023mff,
  author = {Tan, Jinkai and Huang, Qiqiao and Chen, Sheng},
  title = {Deep Learning Model based on Multi-scale Feature Fusion for Precipitation Nowcasting},
  publisher = {Copernicus GmbH},
  year = {2023},
  doi = {10.5194/gmd-2023-109}
}
```

</details>

##### (2023) Latent diffusion models for generative precipitation nowcasting with accurate uncertainty quantification
* Venue: *arXiv*
* Model: LDCast
* GitHub: https://github.com/MeteoSwiss/ldcast
<details><summary>bibtex</summary>

```bibtex
@misc{leinonen2023ldcast,
  author = {Jussi Leinonen and Ulrich Hamann and Daniele Nerini and Urs Germann and Gabriele Franch},
  title = {Latent diffusion models for generative precipitation nowcasting with accurate uncertainty quantification},
  year = {2023},
  eprint = {2304.12891},
  archivePrefix = {arXiv},
  primaryClass = {physics.ao-ph}
}
```

</details>

##### (2023) PreDiff: Precipitation Nowcasting with Latent Diffusion Models
* Venue: *NeurIPS*
* Model: PreDiff
<details><summary>bibtex</summary>

```bibtex
@inproceedings{gao2023prediff,
  author = {Zhihan Gao and Xingjian Shi and Boran Han and Hao Wang and Xiaoyong Jin and Danielle C. Maddix and Yi Zhu and Mu Li and Yuyang Wang},
  title = {PreDiff: Precipitation Nowcasting with Latent Diffusion Models},
  booktitle = {Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023},
  year = {2023},
  url = {http://papers.nips.cc/paper\_files/paper/2023/hash/f82ba6a6b981fbbecf5f2ee5de7db39c-Abstract-Conference.html}
}
```

</details>

##### (2023) Physical-Dynamic-Driven AI-Synthetic Precipitation Nowcasting Using Task-Segmented Generative Model
* Venue: *Geophysical Research Letters*
* Model: STGM
<details><summary>bibtex</summary>

```bibtex
@article{wang2023stgm,
  author = {Wang, Rui and Fung, Jimmy C. H. and Lau, Alexis K. H.},
  title = {Physical-Dynamic-Driven AI-Synthetic Precipitation Nowcasting Using Task-Segmented Generative Model},
  journal = {Geophysical Research Letters},
  volume = {50},
  number = {21},
  year = {2023},
  doi = {10.1029/2023GL106084}
}
```

</details>

##### (2023) PAUNet: Precipitation Attention-based U-Net for rain prediction from satellite radiance data
* Venue: *arXiv*
* Model: PAUNet
<details><summary>bibtex</summary>

```bibtex
@misc{reddy2023paunet,
  author = {P. Jyoteeshkumar Reddy and Harish Baki and Sandeep Chinta and Richard Matear and John Taylor},
  title = {PAUNet: Precipitation Attention-based U-Net for rain prediction from satellite radiance data},
  year = {2023},
  eprint = {2311.18306},
  archivePrefix = {arXiv},
  primaryClass = {physics.ao-ph}
}
```

</details>

##### (2023) RainAI - Precipitation Nowcasting from Satellite Data
* Venue: *arXiv*
* Model: RainAI
<details><summary>bibtex</summary>

```bibtex
@misc{sarabia2023rainai,
  author = {Rafael Pablos Sarabia and Joachim Nyborg and Morten Birk and Ira Assent},
  title = {RainAI -- Precipitation Nowcasting from Satellite Data},
  year = {2023},
  eprint = {2311.18398},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV}
}
```

</details>

##### (2024) DiffCast: A Unified Framework via Residual Diffusion for Precipitation Nowcasting
* Venue: *CVPR*
* Model: DiffCast
<details><summary>bibtex</summary>

```bibtex
@inproceedings{yu2024diffcast,
  author = {Demin Yu and Xutao Li and Yunming Ye and Baoquan Zhang and Chuyao Luo and Kuai Dai and Rui Wang and Xunlai Chen},
  title = {DiffCast: {A} Unified Framework via Residual Diffusion for Precipitation Nowcasting},
  booktitle = {{IEEE/CVF} Conference on Computer Vision and Pattern Recognition, {CVPR} 2024, Seattle, WA, USA, June 16-22, 2024},
  pages = {27758--27767},
  publisher = {{IEEE}},
  year = {2024},
  doi = {10.1109/CVPR52733.2024.02622}
}
```

</details>

##### (2023) Improving Precipitation Nowcasting for High-Intensity Events Using Deep Generative Models with Balanced Loss and Temperature Data: A Case Study in the Netherlands
* Venue: *Artificial Intelligence for the Earth Systems*
* Model: Balanced Loss and Temperature Data
<details><summary>bibtex</summary>

```bibtex
@article{cambiervannooten2023improving,
  author = {Cambier van Nooten, Charlotte and Schreurs, Koert and Wijnands, Jasper S. and Leijnse, Hidde and Schmeits, Maurice and Whan, Kirien and Shapovalova, Yuliya},
  title = {Improving Precipitation Nowcasting for High-Intensity Events Using Deep Generative Models with Balanced Loss and Temperature Data: A Case Study in the Netherlands},
  journal = {Artificial Intelligence for the Earth Systems},
  volume = {2},
  number = {4},
  year = {2023},
  doi = {10.1175/AIES-D-23-0017.1}
}
```

</details>

##### (2024) CasCast: Skillful High-resolution Precipitation Nowcasting via Cascaded Modelling
* Venue: *arXiv*
* Model: CasCast
<details><summary>bibtex</summary>

```bibtex
@misc{gong2024cascast,
  author = {Junchao Gong and Lei Bai and Peng Ye and Wanghan Xu and Na Liu and Jianhua Dai and Xiaokang Yang and Wanli Ouyang},
  title = {CasCast: Skillful High-resolution Precipitation Nowcasting via Cascaded Modelling},
  year = {2024},
  eprint = {2402.04290},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG}
}
```

</details>

##### (2024) DB-RNN: A RNN for Precipitation Nowcasting Deblurring
* Venue: *IEEE JSTARS*
* Model: DB-RNN
<details><summary>bibtex</summary>

```bibtex
@article{ma2024dbrnn,
  author = {Zhifeng Ma and Hao Zhang and Jie Liu},
  title = {{DB-RNN:} An {RNN} for Precipitation Nowcasting Deblurring},
  journal = {{IEEE} J. Sel. Top. Appl. Earth Obs. Remote. Sens.},
  volume = {17},
  pages = {5026--5041},
  year = {2024},
  doi = {10.1109/JSTARS.2024.3365612}
}
```

</details>

##### (2024) PP-Loss: An imbalanced regression loss based on plotting position for improved precipitation nowcasting
* Venue: *Theoretical and Applied Climatology*
* Model: PP-Loss
<details><summary>bibtex</summary>

```bibtex
@article{xu2024pploss,
  author = {Xu, Lei and Li, Xuechun and Yu, Hongchu and Du, Wenying and Chen, Zeqiang and Chen, Nengcheng},
  title = {PP-Loss: An imbalanced regression loss based on plotting position for improved precipitation nowcasting},
  journal = {Theoretical and Applied Climatology},
  volume = {155},
  number = {7},
  pages = {5909--5923},
  year = {2024},
  doi = {10.1007/s00704-024-04984-w}
}
```

</details>

##### (2024) Hybrid physics-AI outperforms numerical weather prediction for extreme precipitation nowcasting
* Venue: *npj Climate and Atmospheric Science*
<details><summary>bibtex</summary>

```bibtex
@article{das2024hybrid,
  author = {Das, Puja and Posch, August and Barber, Nathan and Hicks, Michael and Duffy, Kate and Vandal, Thomas and Singh, Debjani and van Werkhoven, Katie and Ganguly, Auroop R.},
  title = {Hybrid physics-AI outperforms numerical weather prediction for extreme precipitation nowcasting},
  journal = {npj Climate and Atmospheric Science},
  volume = {7},
  number = {1},
  pages = {282},
  year = {2024},
  doi = {10.1038/s41612-024-00834-8}
}
```

</details>

##### (2025) A Space-Time Transformer for Precipitation Nowcasting
* Venue: *arXiv*
* Model: SaTformer
* GitHub: https://github.com/leharris3/satformer
<!-- * Intro: First place on the NeurIPS Weather4cast 2025 "Cumulative Rainfall" challenge. -->
<details><summary>bibtex</summary>

```bibtex
@misc{harris2025satformer,
  author = {Levi Harris and Tianlong Chen},
  title = {A Space-Time Transformer for Precipitation Nowcasting},
  year = {2025},
  eprint = {2511.11090},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV}
}
```

</details>

:card_file_box: Datasets
==

<!-- ##### (2021) EarthNet2021: A large-scale dataset and challenge for Earth surface forecasting as a guided video prediction task
* Venue: *CVPR Workshop EarthVision*
* Dataset: EarthNet2021
* Paper: https://openaccess.thecvf.com/content/CVPR2021W/EarthVision/html/Requena-Mesa_EarthNet2021_A_Large-Scale_Dataset_and_Challenge_for_Earth_Surface_Forecasting_CVPRW_2021_paper.html
* Doc: https://www.earthnet.tech/
* GitHub: https://github.com/earthnet2021/earthnet-model-intercomparison-suite -->

### NOAA <img src="https://www.google.com/s2/favicons?domain=noaa.gov&sz=64" height="40" align="center" alt="NOAA logo">
---

##### (2016) Multi-Radar Multi-Sensor (MRMS) Quantitative Precipitation Estimation: Initial Operating Capabilities
* Venue: *Bulletin of the American Meteorological Society*
* Dataset: MRMS
* Doc: https://www.nssl.noaa.gov/projects/mrms/
<details><summary>bibtex</summary>

```bibtex
@article{zhang2016mrms,
  author = {Zhang, Jian and Howard, Kenneth and Langston, Carrie and Kaney, Brian and Qi, Youcun and Tang, Lin and Grams, Heather and Wang, Yadong and Cocks, Stephen and Martinaitis, Steven and Arthur, Ami and Cooper, Karen and Brogden, Jeff and Kitzmiller, David},
  title = {Multi-Radar Multi-Sensor (MRMS) Quantitative Precipitation Estimation: Initial Operating Capabilities},
  journal = {Bulletin of the American Meteorological Society},
  volume = {97},
  number = {4},
  pages = {621--638},
  year = {2016},
  doi = {10.1175/BAMS-D-14-00174.1}
}
```

</details>

### Others
---

##### (2021) RainBench: Towards Global Precipitation Forecasting from Satellite Imagery
* Venue: *AAAI*
* Dataset: RainBench
* GitHub: https://github.com/FrontierDevelopmentLab/PyRain
<details><summary>bibtex</summary>

```bibtex
@inproceedings{dewitt2021rainbench,
  author = {Christian Schr{\"{o}}der de Witt and Catherine Tong and Valentina Zantedeschi and Daniele De Martini and Alfredo Kalaitzis and Matthew Chantry and Duncan Watson{-}Parris and Piotr Bilinski},
  title = {RainBench: Towards Data-Driven Global Precipitation Forecasting from Satellite Imagery},
  booktitle = {Thirty-Fifth {AAAI} Conference on Artificial Intelligence, {AAAI} 2021, Thirty-Third Conference on Innovative Applications of Artificial Intelligence, {IAAI} 2021, The Eleventh Symposium on Educational Advances in Artificial Intelligence, {EAAI} 2021, Virtual Event, February 2-9, 2021},
  pages = {14902--14910},
  publisher = {{AAAI} Press},
  year = {2021},
  doi = {10.1609/aaai.v35i17.17749}
}
```

</details>

##### (2022) Benchmark Dataset for Precipitation Forecasting by Post-Processing the Numerical Weather Prediction
* Venue: *arXiv*
* Dataset: KoMet
* GitHub: https://github.com/osilab-kaist/KoMet-Benchmark-Dataset
<details><summary>bibtex</summary>

```bibtex
@misc{kim2022komet,
  author = {Taehyeon Kim and Namgyu Ho and Donggyu Kim and Se-Young Yun},
  title = {Benchmark Dataset for Precipitation Forecasting by Post-Processing the Numerical Weather Prediction},
  year = {2022},
  eprint = {2206.15241},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG}
}
```

</details>

##### (2024) PostRainBench: A Comprehensive Benchmark and a New Model for Precipitation Forecasting
* Venue: *arXiv*
* Dataset: PostRainBench
* GitHub: https://github.com/yyyujintang/PostRainBench
<details><summary>bibtex</summary>

```bibtex
@misc{tang2024postrainbench,
  author = {Yujin Tang and Jiaming Zhou and Xiang Pan and Zeying Gong and Junwei Liang},
  title = {PostRainBench: A comprehensive benchmark and a new model for precipitation forecasting},
  year = {2024},
  eprint = {2310.02676},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG}
}
```

</details>

:calendar: Workshops
==

##### (2022) Tackling Climate Change with Machine Learning
* Venue: *NeurIPS*
* Link: https://www.climatechange.ai/events/neurips2022

##### (2023) Tackling Climate Change with Machine Learning: Blending New and Existing Knowledge Systems
* Venue: *NeurIPS*
* Link: https://neurips.cc/virtual/2023/workshop/66543

##### (2023) Weather4cast
* Venue: *NeurIPS competition*
* Link: https://weather4cast.net/

##### (2024) Weather4cast
* Venue: *NeurIPS competition*
* Link: https://weather4cast.net/neurips2024/

##### (2025) Weather4cast
* Venue: *NeurIPS competition*
<!-- * Intro: Multi-task challenges for weather & pollution pattern prediction on the road to hi-res foundation models: super-resolution rain movies, cumulative rainfall, severe weather events, and (new for 2025) atmospheric pollution forecasting. -->
* Link: https://weather4cast.net/neurips2025/, https://neurips.cc/virtual/2025/competition/127725

:package: Libraries
==

##### (2016) The Python ARM Radar Toolkit (Py-ART), a Library for Working with Weather Radar Data in the Python Programming Language
* Venue: *Journal of Open Research Software*
* Library: Py-ART
<!-- * Intro: A data model driven interactive toolkit for working with weather radar data. -->
* Doc: https://arm-doe.github.io/pyart/
* GitHub: https://github.com/ARM-DOE/pyart
<details><summary>bibtex</summary>

```bibtex
@article{helmus2016pyart,
  author = {Helmus, Jonathan J and Collis, Scott M},
  title = {The Python ARM Radar Toolkit (Py-ART), a Library for Working with Weather Radar Data in the Python Programming Language},
  journal = {Journal of Open Research Software},
  volume = {4},
  number = {1},
  pages = {25},
  year = {2016},
  doi = {10.5334/jors.119}
}
```

</details>

##### (2013) Technical Note: An open source library for processing weather radar data (wradlib)
* Venue: *Hydrology and Earth System Sciences*
* Library: wradlib
<!-- * Intro: An open source library for weather radar data processing. -->
* Doc: https://docs.wradlib.org/en/stable/
* GitHub: https://github.com/wradlib/wradlib
<details><summary>bibtex</summary>

```bibtex
@article{heistermann2013wradlib,
  author = {Heistermann, M. and Jacobi, S. and Pfaff, T.},
  title = {Technical Note: An open source library for processing weather radar data (wradlib)},
  journal = {Hydrology and Earth System Sciences},
  volume = {17},
  number = {2},
  pages = {863--871},
  year = {2013},
  doi = {10.5194/hess-17-863-2013}
}
```

</details>

##### (2010) Cartopy: a cartographic Python library with a Matplotlib interface
* Venue: *Met Office*
* Library: Cartopy
<!-- * Intro: A Python package designed to make drawing maps for data analysis and visualisation easy. -->
* Doc: https://scitools.org.uk/cartopy/docs/latest/
* GitHub: https://github.com/SciTools/cartopy
<details><summary>bibtex</summary>

```bibtex
@manual{cartopy,
  author = {{Met Office}},
  title = {Cartopy: a cartographic {Python} library with a {Matplotlib} interface},
  address = {Exeter, Devon},
  year = {2010 - 2015},
  url = {https://cartopy.readthedocs.io}
}
```

</details>

##### Satflow
* Library: Satflow
<!-- * Intro: Satellite optical flow with machine learning models. -->
* Doc: https://satflow.readthedocs.io/en/stable/
* GitHub: https://github.com/openclimatefix/satflow

<!-- ##### Google Earth Engine API
* Library: Google Earth Engine API
<!-- * Intro: Python and JavaScript bindings for calling the Earth Engine API. -->
* Doc: https://earthengine.google.com/
* GitHub: https://github.com/google/earthengine-api -->

<!-- ##### OpenSTL: A Comprehensive Benchmark of Spatio-Temporal Predictive Learning
* Library: OpenSTL
* Doc: https://openstl.readthedocs.io/en/latest/
* GitHub: https://github.com/chengtan9907/OpenSTL -->

<!-- ##### (2023) WeatherBench 2
* Venue: *arXiv*
* Library: WeatherBench 2
<!-- * Intro: A benchmark for the next generation of data-driven global weather models. -->
* Paper: https://arxiv.org/abs/2308.15560
* Doc: https://blog.research.google/2023/08/weatherbench-2-benchmark-for-next.html
* GitHub: https://github.com/google-research/weatherbench2 -->

<!--
:link: Others
==
##### EarthArXiv
<!-- * Intro: EarthArXiv publishes articles from all subdomains of Earth Science and related domains of planetary science. -->
* Link: https://eartharxiv.org/repository/about/

##### Awesome-Foundation-Models-for-Weather-and-Climate
<!-- * Intro: A survey of foundation models for weather and climate data understanding. -->
* GitHub: https://github.com/shengchaochen82/Awesome-Foundation-Models-for-Weather-and-Climate

##### Awesome Large Weather Models
<!-- * Intro: A collection of awesome Large Weather Models (LWMs) | AI for Earth (AI4Earth) | AI for Science (AI4Science) -->
* GitHub: https://github.com/jaychempan/Awesome-LWMs -->
