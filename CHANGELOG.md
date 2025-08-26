# [4.7.0](https://github.com/QueroDelivery/ci/compare/v4.6.0...v4.7.0) (2025-08-26)


### Features

* **readme:** change example workflows of stage environment ([3317735](https://github.com/QueroDelivery/ci/commit/331773549a6a1882bccd3c5ea177ccf8a4b45d99))

# [4.6.0](https://github.com/QueroDelivery/ci/compare/v4.5.0...v4.6.0) (2025-08-26)


### Features

* **readme:** change s3 readme to use a new method to define variables to each environment ([bb882ce](https://github.com/QueroDelivery/ci/commit/bb882cea5e41e65a0e5bf8c6084acad3e27181a8))
* **readme:** change s3 readme to use a new method to define variables to each environment ([1fbfd43](https://github.com/QueroDelivery/ci/commit/1fbfd4307b712ea5768aca64f0f596ea41f6c049))

# [4.5.0](https://github.com/QueroDelivery/ci/compare/v4.4.0...v4.5.0) (2025-08-26)


### Features

* **credentials:** disable persistence ([767786d](https://github.com/QueroDelivery/ci/commit/767786da27826b12610e1aaead31337d47899937))

# [4.4.0](https://github.com/QueroDelivery/ci/compare/v4.3.0...v4.4.0) (2025-08-25)


### Features

* **node:** adds logic to install dependencies ([a91f42b](https://github.com/QueroDelivery/ci/commit/a91f42b4565e27d85e1d7e6adbcda8176052a1e3))

# [4.3.0](https://github.com/QueroDelivery/ci/compare/v4.2.0...v4.3.0) (2025-08-25)


### Features

* **publish:** adds checkout step ([6b96a70](https://github.com/QueroDelivery/ci/commit/6b96a706b588fd85715f0c7515803ea0cfddb606))

# [4.2.0](https://github.com/QueroDelivery/ci/compare/v4.1.1...v4.2.0) (2025-08-19)


### Features

* **ci-s3:** automates the deployment of static apps to S3 with auto CloudFront cache invalidation ([fddffb8](https://github.com/QueroDelivery/ci/commit/fddffb8579aabc3bba0f37b4b377d55f25ded164))
* **flows:** adds diagram flows to each step ([e7a1484](https://github.com/QueroDelivery/ci/commit/e7a1484ca10515f725633f1ac830c6767a2d9dd1))
* **structure:** adds a new structure to enhance handling with environments and conditions ([18cdabe](https://github.com/QueroDelivery/ci/commit/18cdabe8c1823853e98ff7d4a0dd8dab07686855))
* **structure:** create a new file responsible to clear last uploaded preview ([0736f0a](https://github.com/QueroDelivery/ci/commit/0736f0a6624738f37652c36f94398f9c02a02ee3))

## [4.1.1](https://github.com/QueroDelivery/ci/compare/v4.1.0...v4.1.1) (2025-08-18)


### Bug Fixes

* streamline git fetch and commit process in CI workflow ([237e687](https://github.com/QueroDelivery/ci/commit/237e687b76f0e912fbb3edc4915a77fb125d577d))

# [4.1.0](https://github.com/QueroDelivery/ci/compare/v4.0.3...v4.1.0) (2025-08-18)


### Bug Fixes

* rename prop to keep the same pattern ([27d8039](https://github.com/QueroDelivery/ci/commit/27d8039379c0b04cf1784f7cf52b5d928f1e52b1))
* rm unnecessary param ([59ba2c8](https://github.com/QueroDelivery/ci/commit/59ba2c897b62f88da0c77481d6a4a294273a4671))


### Features

* adding build python apps ([2f8b86c](https://github.com/QueroDelivery/ci/commit/2f8b86ca70d50cf795c3a5ff8a662cb54df00ae2))
* use service name as input and read from pjson when it doesn't provide ([4b3def7](https://github.com/QueroDelivery/ci/commit/4b3def769dbd4256845dba1205e517e1002a42ab))

## [4.0.3](https://github.com/QueroDelivery/ci/compare/v4.0.2...v4.0.3) (2025-08-15)


### Bug Fixes

* add feature back that override kube files when it configured on github ([f7e5b90](https://github.com/QueroDelivery/ci/commit/f7e5b905847f4bbd7b0320ecd95c5b051daf838f))

## [4.0.2](https://github.com/QueroDelivery/ci/compare/v4.0.1...v4.0.2) (2025-08-12)


### Bug Fixes

* error 254 in promote ([dc7745b](https://github.com/QueroDelivery/ci/commit/dc7745bcae5d795640d866b295f0c5cb4bc0fc75))
* mistake on retag step ([188f088](https://github.com/QueroDelivery/ci/commit/188f088b4a079b15975d00c0398f2756432ec985))

## [4.0.1](https://github.com/QueroDelivery/ci/compare/v4.0.0...v4.0.1) (2025-08-04)


### Bug Fixes

* commit message ([48ba000](https://github.com/QueroDelivery/ci/commit/48ba000c0fa99c1f8bdc90af80b3a77ba3dca241))
* mkdir before copy file in deploy state ([b7d857f](https://github.com/QueroDelivery/ci/commit/b7d857fbf5b1c97f44e99069aae79f34b720275c))

# [4.0.0](https://github.com/QueroDelivery/ci/compare/v3.5.1...v4.0.0) (2025-08-04)


### Bug Fixes

* a few path mismatch ([3578d1f](https://github.com/QueroDelivery/ci/commit/3578d1f715569e99617baea75dca6269117f9c81))
* add coment with app review link ([e2bf318](https://github.com/QueroDelivery/ci/commit/e2bf318e8236f6da636e017cd3c6e783eb6a2e22))
* add login ecr before retag ([eac47c1](https://github.com/QueroDelivery/ci/commit/eac47c1fb8c35805014472b42aaaf5990953f99b))
* add update file with new params on upsert service json ([a55af9d](https://github.com/QueroDelivery/ci/commit/a55af9dca8fd32f3a1aade73168d821e8850722e))
* commit service json ([6292790](https://github.com/QueroDelivery/ci/commit/6292790aba452e7142904bd45a98f7d1658575cf))
* cp service json independent environment ([a9db3e1](https://github.com/QueroDelivery/ci/commit/a9db3e1f40ef7c39eb01bb6de7336d578c5f8a0c))
* create PR to main with upsert behavior ([f766806](https://github.com/QueroDelivery/ci/commit/f7668064b7be2a0418590f6235361fedd527c3dd))
* create service json when doesnt exists ([1bd72a6](https://github.com/QueroDelivery/ci/commit/1bd72a69ba2cb0edfd35e6ddc54cad8940acb885))
* dont tag dev in ecr ([7eafb3e](https://github.com/QueroDelivery/ci/commit/7eafb3e541b7dca00a3bf006ee8e4414df0825be))
* ecr name on push ([8182696](https://github.com/QueroDelivery/ci/commit/81826962cde91fa3734bd44e870f3a99609ccd11))
* ensure deploy state branch exists ([0939118](https://github.com/QueroDelivery/ci/commit/0939118ccb02e547d68487d9ebb93637b26ffc34))
* export correct digest after push ecr ([94d140f](https://github.com/QueroDelivery/ci/commit/94d140fd3404a7709732553ce80a90f0f9a9b3d8))
* export servicename on promote ([54b3f0a](https://github.com/QueroDelivery/ci/commit/54b3f0af132a12d8aee97c8db9a22354d81c79f7))
* fetch correct service json ([41ac03b](https://github.com/QueroDelivery/ci/commit/41ac03bbed7e37bf0510d29225997ffacf7aa93a))
* name of state file in artifact ([017cb76](https://github.com/QueroDelivery/ci/commit/017cb7679515ee64b203dffc96f4fa2d996bcf48))
* overriding service json file ([7478c2b](https://github.com/QueroDelivery/ci/commit/7478c2b2574669c1a8bb94191ee4340d4dbfaf6a))
* overriding services json ([e3f939c](https://github.com/QueroDelivery/ci/commit/e3f939c9fec4ba67a4ab94a7c6ee05099ac95196))
* parameters on setup aws ([905bba9](https://github.com/QueroDelivery/ci/commit/905bba95180291a800375219fb529f383d498242))
* path reading values from service json ([451eff4](https://github.com/QueroDelivery/ci/commit/451eff4d0458abfe8e5794fcb4b40ecb363b633a))
* promote reading metadata ([d402d29](https://github.com/QueroDelivery/ci/commit/d402d296279e60100b880976791299b7776c963e))
* push flow of updated service files ([93c42e7](https://github.com/QueroDelivery/ci/commit/93c42e7b7cd2700eeae87bd814b43ccaec4f1176))
* repository name in ecr ([9bce038](https://github.com/QueroDelivery/ci/commit/9bce0381f432814b9679564bd23297050106c61c))
* retag image flow ([67287d7](https://github.com/QueroDelivery/ci/commit/67287d7f41becc7047e7ecdb11c5110cf4f91971))
* rm unnecessary cat ([0d1e28f](https://github.com/QueroDelivery/ci/commit/0d1e28f7f628dc123b1d3ea01a4f6e8abda8b860))
* rm unnecessary input on push ecr ([40abbe6](https://github.com/QueroDelivery/ci/commit/40abbe6e7f8127f90fc735b19ab7c9aeca579a4e))
* rollback to remove kube cpu limit when null ([74989de](https://github.com/QueroDelivery/ci/commit/74989de3406622b3860408e430d9c9f0ddce0ac6))
* rules to breaking change on semantic release ([d56ff34](https://github.com/QueroDelivery/ci/commit/d56ff3429c658ef9aa647e2467161ff9fdcf4640))
* secret instead input ([1a5e623](https://github.com/QueroDelivery/ci/commit/1a5e623f0988f7652e342d3759995bcedc08a7dc))
* setup npmrc step ([faa2f4b](https://github.com/QueroDelivery/ci/commit/faa2f4ba9915f22577de9e39150d6e15be39ba61))
* update file locally and remotelly ([ea3ffda](https://github.com/QueroDelivery/ci/commit/ea3ffda6e64a76ce058f409aaabc1961735084f1))
* upsert service json in repository ([f58c3c1](https://github.com/QueroDelivery/ci/commit/f58c3c182eefc721737569190e488b6c0c5d2ed1))
* version tag promoted ([44d156c](https://github.com/QueroDelivery/ci/commit/44d156c283a10eb317cc2a638c1a40d04ee95cc0))
* version_tag as output to push ecr process ([f075825](https://github.com/QueroDelivery/ci/commit/f07582509675dc9c9b5e8a8b43a519ab949d9112))
* wrong initial command ([ea6b0d2](https://github.com/QueroDelivery/ci/commit/ea6b0d2c8d115bec3e1436a74ff6016bddd201ec))


### Features

* add promote steps ([40c1e28](https://github.com/QueroDelivery/ci/commit/40c1e28a247484ccee7cd49ed8a7f03c9828d080))
* add retag idempotent process ([e00452b](https://github.com/QueroDelivery/ci/commit/e00452b593aa7db2e11b55f4c2fc0253359bf324))
* add retag image in ecr ([9539efd](https://github.com/QueroDelivery/ci/commit/9539efd70822aa1ffdd0cdfb741f3573b27ef8a7))
* adding new packages to run release locally ([c3f3de2](https://github.com/QueroDelivery/ci/commit/c3f3de244b191d3da4aa51fc2fe541724d5f2ac1))
* commit deploy state in separately branch ([f499fd1](https://github.com/QueroDelivery/ci/commit/f499fd1e92e53216d769927dcfcf363f70a16c13))
* ensure deploy state branch exists ([6f4ed83](https://github.com/QueroDelivery/ci/commit/6f4ed830849b42b11f4ba519c85bdb668abe9d26))
* export digest after push ecr ([5906f9d](https://github.com/QueroDelivery/ci/commit/5906f9d3a7e6e58c8f4b6faf5511b922485ba900))
* general ci changes to able build once deploy many ([fae374d](https://github.com/QueroDelivery/ci/commit/fae374d103ef461d344acef8d3bb24321212ce01))
* general updates in service json file ([ce3629a](https://github.com/QueroDelivery/ci/commit/ce3629a9ddbc1ce87ff6c5b216deebda301a858d))
* generating BREAKING CHANGE ([83649dc](https://github.com/QueroDelivery/ci/commit/83649dce4c57efe0b9e01e58a4555037a23af770))
* idempotency on commit service json ([5c2059e](https://github.com/QueroDelivery/ci/commit/5c2059edc4d3c5161c22d8d5aeb5226eea336ae3))
* just upload to deploy-state in stg or prd ([a7ee493](https://github.com/QueroDelivery/ci/commit/a7ee493be8834cda0499ee1628cb577128ebfcc2))
* receive a WF_IMAGE_VERSION_TAG on deploy ([13993eb](https://github.com/QueroDelivery/ci/commit/13993eb849419cbf0b9d4955d07edfa8da68e1f1))
* set version tag as an output ([b6cee69](https://github.com/QueroDelivery/ci/commit/b6cee6931dbf72b9c0a0bc4d84e27d20379e1eea))
* use digest image instead just a tag ([4569851](https://github.com/QueroDelivery/ci/commit/45698517b239a8c23c32729aee22274248e44216))
* use image digest to upsert service.json file ([c226b50](https://github.com/QueroDelivery/ci/commit/c226b50341ce6b8313845910238e153f6b92fba0))

## [3.5.1](https://github.com/QueroDelivery/ci/compare/v3.5.0...v3.5.1) (2025-05-06)


### Bug Fixes

* cpu limit configs ([845da1a](https://github.com/QueroDelivery/ci/commit/845da1a0c9238543fe516c19ff810180ba89244a))
* kube folder path ([cd8fd98](https://github.com/QueroDelivery/ci/commit/cd8fd988f964dc3ec9bde9808a28baf4d01f11d0))

# [3.5.0](https://github.com/QueroDelivery/ci/compare/v3.4.0...v3.5.0) (2025-04-23)


### Features

* use new kube folder ([98900fc](https://github.com/QueroDelivery/ci/commit/98900fc9acf1c76bcd85bf0558595c6494792260))

# [3.4.0](https://github.com/QueroDelivery/ci/compare/v3.3.0...v3.4.0) (2024-11-08)


### Features

* upgrade kubectl version ([c24d6b7](https://github.com/QueroDelivery/ci/commit/c24d6b7982ff2bcf229d5819c50acb403a0ed556))

# [3.3.0](https://github.com/QueroDelivery/ci/compare/v3.2.0...v3.3.0) (2024-11-07)


### Features

* lock version of kube folder ([743c0bf](https://github.com/QueroDelivery/ci/commit/743c0bff95f68ab9cfbf81f443c32c34be5311ca))

# [3.2.0](https://github.com/QueroDelivery/ci/compare/v3.1.0...v3.2.0) (2024-10-16)


### Features

* **new-env-font-awesome:** Should add new input and new env referr of fontAwesome ([ac3c6ab](https://github.com/QueroDelivery/ci/commit/ac3c6abefab0ad6c7bdbfebc3855d45daae1e3ba))

# [3.1.0](https://github.com/QueroDelivery/ci/compare/v3.0.0...v3.1.0) (2024-09-03)


### Bug Fixes

* rollback curl aws-iam-authenticator version ([655e642](https://github.com/QueroDelivery/ci/commit/655e6420d4dea64c5694ff6f71180b0c96d99f4e))


### Features

* fixed version of kube folder ([8155038](https://github.com/QueroDelivery/ci/commit/815503857699adbc80ee025560eb7d65126bd09b))
* update aws iam authenticator bin version ([f7d1f06](https://github.com/QueroDelivery/ci/commit/f7d1f064c6629f7b8dd08f9a7c9fc7c620c7f6a6))
* upgrade kubectl version to 1.28 ([3f1738c](https://github.com/QueroDelivery/ci/commit/3f1738cf8a155920b02c22512a277a441289d306))

# [3.0.0](https://github.com/QueroDelivery/ci/compare/v2.13.0...v3.0.0) (2024-09-03)


### Bug Fixes

* change WF_INTERNET_FACING to required false and default false ([e91de17](https://github.com/QueroDelivery/ci/commit/e91de17df87f5107c77ebc80d37703b597c5f5a1))
* revert internet-facing ([26b5031](https://github.com/QueroDelivery/ci/commit/26b50317970ead5219704cd7bf3ff047ebb89d35))


### Features

* add feature to configure non internet facing ([fc1526c](https://github.com/QueroDelivery/ci/commit/fc1526c3432f39a5266552eb541772e7c641feb5))
* turn memory requested optional and default 250Mi ([3319975](https://github.com/QueroDelivery/ci/commit/33199754788c1bf6684b516b300cbe36bbd92b51))
* upgrade kube folder version ([5da2a76](https://github.com/QueroDelivery/ci/commit/5da2a769f3e3a3a8bac1b1a85b4fa849758e8c9a))


### BREAKING CHANGES

* This commit needs to set a new variable to configure
the visibility of the service.
If the Service is internet facing you should configure the
WF_INTERNET_FACING: TRUE, Otherwise , its value is false.

footer: This commit is needed to set the visibility of the services on
internet facing or local

# [2.13.0](https://github.com/QueroDelivery/ci/compare/v2.12.0...v2.13.0) (2024-06-21)


### Features

* :sparkles: update version amazon-ecr-login and configure-aws-credentials ([58d12b0](https://github.com/QueroDelivery/ci/commit/58d12b0233b48473dfc11dd757bc4f40f35968ce))

# [2.12.0](https://github.com/QueroDelivery/ci/compare/v2.11.0...v2.12.0) (2024-06-18)


### Features

* fixed version of kube folder ([5d65efb](https://github.com/QueroDelivery/ci/commit/5d65efbbbb38a02c5fc34b5a059209da21b44292))

# [2.11.0](https://github.com/QueroDelivery/ci/compare/v2.10.0...v2.11.0) (2024-06-07)


### Features

* :sparkles: update checkout, setup-node and cache to v4 ([70795dd](https://github.com/QueroDelivery/ci/commit/70795dd15776da0544130bd5984e9cd95c3c0b58))
* :sparkles: update checkout, setup-node and cache to v4 ([488ff8f](https://github.com/QueroDelivery/ci/commit/488ff8fa3e5032763814c1bca7df866409481956))

# [2.10.0](https://github.com/QueroDelivery/ci/compare/v2.9.0...v2.10.0) (2023-12-15)


### Bug Fixes

* directory to  kube folder ([3549d67](https://github.com/QueroDelivery/ci/commit/3549d67889bca0844963255b0c146413fcd6ccc9))
* if command on remove WF KUBE CPU LIMIT ([011215b](https://github.com/QueroDelivery/ci/commit/011215b86e601e105fb83ea8e79ac93f98444fda))
* if condition ([a318cf0](https://github.com/QueroDelivery/ci/commit/a318cf0752919efadf5510a16d0a14f35347d5b9))
* if statement ([25ac13b](https://github.com/QueroDelivery/ci/commit/25ac13bc439e0a1a9c2183a4a4a9822a683dbed0))
* nil string ([9d2a403](https://github.com/QueroDelivery/ci/commit/9d2a40310040307e0e7cb2a05a67b6ff807b523b))


### Features

* turn WF_KUBE_CPU_LIMIT optional and remove it from config when is null ([84a73b5](https://github.com/QueroDelivery/ci/commit/84a73b5ad182954b8e85745f927c422fc88435e6))

# [2.9.0](https://github.com/QueroDelivery/ci/compare/v2.8.0...v2.9.0) (2023-12-12)


### Bug Fixes

* exporting WF_KUBE_MEMORY_LIMIT ([1b04257](https://github.com/QueroDelivery/ci/commit/1b04257f0cab3d577118bc609deb59ff0f298441))


### Features

* defining memory limit as memory requested when doesn't send memory limit input ([2ce7a08](https://github.com/QueroDelivery/ci/commit/2ce7a08f34b0e140367a8aa753e34721d77cc0b3))

# [2.8.0](https://github.com/QueroDelivery/ci/compare/v2.7.0...v2.8.0) (2023-12-12)


### Bug Fixes

* defining cpu requested instead cpu limits default ([0264ffe](https://github.com/QueroDelivery/ci/commit/0264ffe743b45d1067349c7bca2dcc48d32c0f16))


### Features

* defining default value to cpu requested ([108a340](https://github.com/QueroDelivery/ci/commit/108a340256a411b3ead9c07d8d4bcb6fd671ca7e))
* defining default value to memory requested ([4524aeb](https://github.com/QueroDelivery/ci/commit/4524aebd2506aa49a5493da1f8ee72d1367ae13b))

# [2.7.0](https://github.com/QueroDelivery/ci/compare/v2.6.1...v2.7.0) (2023-09-18)


### Features

* define kube folder version ([b839f2b](https://github.com/QueroDelivery/ci/commit/b839f2b3ba70a56b10296945de7a6c56ef315fa2))
* update bin kubectl ([9ea50f2](https://github.com/QueroDelivery/ci/commit/9ea50f222a3a53c20aa6f593aec51ae95ee745a2))

## [2.6.1](https://github.com/QueroDelivery/ci/compare/v2.6.0...v2.6.1) (2023-08-23)


### Bug Fixes

* add mask password to another steps ([848011e](https://github.com/QueroDelivery/ci/commit/848011e5324b372a740edeeadbc3e9bf2d0728fe))

# [2.6.0](https://github.com/QueroDelivery/ci/compare/v2.5.1...v2.6.0) (2023-08-23)


### Features

* enable mask password as true on ecr login ([27a2cdb](https://github.com/QueroDelivery/ci/commit/27a2cdbd05f1704ae78643b19f9c2fb070c93a22))

## [2.5.1](https://github.com/QueroDelivery/ci/compare/v2.5.0...v2.5.1) (2023-08-18)


### Bug Fixes

* rollback on kube folder ([66aa657](https://github.com/QueroDelivery/ci/commit/66aa6573ceb42a5fd36739a5b0df0df90ed13212))

# [2.5.0](https://github.com/QueroDelivery/ci/compare/v2.4.0...v2.5.0) (2023-08-17)


### Bug Fixes

* check commits shell script step ([f27a053](https://github.com/QueroDelivery/ci/commit/f27a053eebbfefcdb26d2724de35462a323ecb0d))
* just check commits when is to open PR ([7e7221a](https://github.com/QueroDelivery/ci/commit/7e7221a6c3e32e50630da8444372922c2b01eb39))
* run ([8ad25a5](https://github.com/QueroDelivery/ci/commit/8ad25a53d78961a2bd8b5136af1118f0ddaee124))
* syntax shell step ([1a75306](https://github.com/QueroDelivery/ci/commit/1a75306e33941f0a1c5dcf2ef385f40f98d107c3))
* try a different approach to check diff commits count ([092fef2](https://github.com/QueroDelivery/ci/commit/092fef23a8345e8ce802bc270638cfd189c497de))
* try another git command ([28a974e](https://github.com/QueroDelivery/ci/commit/28a974e7c68b4c65aee57eda0ee02ef63e44c083))


### Features

* add check if there is commits between stg to main ([45e755e](https://github.com/QueroDelivery/ci/commit/45e755e32eb734b4e80bbd833dd1de025a37f63d))
* checking if there is any commit ahead main before to pr ([0a22439](https://github.com/QueroDelivery/ci/commit/0a224397a8dc18951655cb37e70e3416b7f10b10))
* config fetch depth on checkout ([1f16f5b](https://github.com/QueroDelivery/ci/commit/1f16f5b2bd6caf3c079365d5a7b68cbcaa38a2c7))

# [2.4.0](https://github.com/QueroDelivery/ci/compare/v2.3.0...v2.4.0) (2023-08-11)


### Features

* upgrade kube files version ([20e6f07](https://github.com/QueroDelivery/ci/commit/20e6f07cf58232934f1ce0fe43f23708c9f0022d))
* use upgrade hpa kube version ([e93abe1](https://github.com/QueroDelivery/ci/commit/e93abe16965645f0319913b52a8f08796dc7be7b))

# [2.3.0](https://github.com/QueroDelivery/ci/compare/v2.2.0...v2.3.0) (2023-07-20)


### Features

* :construction_worker: adding node modules cache to base-node-build workflow ([d701fe8](https://github.com/QueroDelivery/ci/commit/d701fe820ca9f564e2d5594090ab9688684f7843))

# [2.2.0](https://github.com/QueroDelivery/ci/compare/v2.1.1...v2.2.0) (2023-06-28)


### Features

* add create dotenv before build ([9012216](https://github.com/QueroDelivery/ci/commit/90122161a18e47e483ac5a41959abd716cad6652))
* add create dotenv before build ([16bc9e6](https://github.com/QueroDelivery/ci/commit/16bc9e6043a16c91e398b2e87cabb4cc498d5d34))
* add create dotenv before build ([2d973bb](https://github.com/QueroDelivery/ci/commit/2d973bbd117821ee485f68c9ee7acc68f67d816e))
* add create dotenv before build ([5633b21](https://github.com/QueroDelivery/ci/commit/5633b219c4ac4a85ec0fd474c903124f50cc1f44))

## [2.1.1](https://github.com/QueroDelivery/ci/compare/v2.1.0...v2.1.1) (2023-05-25)


### Bug Fixes

* improving log when can't send a coverage report to dev portal ([51bbf8e](https://github.com/QueroDelivery/ci/commit/51bbf8edbb5d2fe4fe3c8ca40149f0e49a7f4e7a))

# [2.1.0](https://github.com/QueroDelivery/ci/compare/v2.0.0...v2.1.0) (2023-05-24)


### Features

* add a internal ingress to application ([dca7324](https://github.com/QueroDelivery/ci/commit/dca732469cce8959026a97b1e8aa226ccedd5ca3))

# [2.0.0](https://github.com/QueroDelivery/ci/compare/v1.35.0...v2.0.0) (2023-03-23)


### Bug Fixes

* add WF_ENV_TYPE_DEPLOY ([efd0201](https://github.com/QueroDelivery/ci/commit/efd02019b29bd08ea1fda1f3b076b22bdb230475))


### Features

* add envtime variable as required ([e19c38d](https://github.com/QueroDelivery/ci/commit/e19c38d168ea0abaa05a3f65059917052aab2cbf))


### BREAKING CHANGES

* This commit breaks the previous versions because
adds the WF_ENV_TYPE as required in the base_node_build.yml file.

This commit changes the CI/CD files to use ${{inputs.WF_ENV_TYPE}}
as job environment.
Example:
jobs:
  setup:
    environment: ${{inputs.WF_ENV_TYPE}}

 On branch feat/add-envtype
 Changes to be committed:
	modified:   .github/workflows/base_build_push_ecr.yml
	modified:   .github/workflows/base_node_build.yml
	modified:   .github/workflows/ci_k8_base.yml
	modified:   .github/workflows/ci_k8_undeploy_base.yml

footer: this commit is related to inprovments on CI/CD asked by Junior

# [1.35.0](https://github.com/QueroDelivery/ci/compare/v1.34.2...v1.35.0) (2023-02-20)


### Features

* adding publish code coverage on ci steps ([2c1344f](https://github.com/QueroDelivery/ci/commit/2c1344f788ea5e0e818e5ecf983c8db5d2c28ec3))

## [1.34.2](https://github.com/QueroDelivery/ci/compare/v1.34.1...v1.34.2) (2023-02-07)


### Bug Fixes

* upgrade version ([3fd20a4](https://github.com/QueroDelivery/ci/commit/3fd20a4a65063df640221944a8a8fec45f5519a5))

## [1.34.1](https://github.com/QueroDelivery/ci/compare/v1.34.0...v1.34.1) (2023-02-01)


### Bug Fixes

* force fix commit ([63249a7](https://github.com/QueroDelivery/ci/commit/63249a791a15ab03ab684527a084d747feb4031c))

# [1.34.0](https://github.com/QueroDelivery/ci/compare/v1.33.0...v1.34.0) (2023-01-28)


### Features

* :construction_worker: update base_node_build.yml to add lint check ([f19ba83](https://github.com/QueroDelivery/ci/commit/f19ba832cf374e48b45e87f391d9f8ffb00a2973))

# [1.33.0](https://github.com/QueroDelivery/ci/compare/v1.32.0...v1.33.0) (2022-12-01)


### Features

* add creating PR Deploy in Prod ([6dd4204](https://github.com/QueroDelivery/ci/commit/6dd4204d289e95d97571636661bc78d1cb931a79))

# [1.32.0](https://github.com/QueroDelivery/ci/compare/v1.31.0...v1.32.0) (2022-11-30)


### Features

* add 20 min of the timeout on undeploy ([f690767](https://github.com/QueroDelivery/ci/commit/f69076761688127ca08855fdb9ed98153a502dcf))

# [1.31.0](https://github.com/QueroDelivery/ci/compare/v1.30.0...v1.31.0) (2022-11-18)


### Features

* add timeout on Kubernets Undeploy. ([b27c298](https://github.com/QueroDelivery/ci/commit/b27c298977a847d813e6de268878c836c4ff4947))

# [1.30.0](https://github.com/QueroDelivery/ci/compare/v1.29.1...v1.30.0) (2022-11-04)


### Features

* update version of ci ([fa11462](https://github.com/QueroDelivery/ci/commit/fa1146204dc351ae71f0d7ca90f962e6dde00853))

# [1.29.0](https://github.com/QueroDelivery/ci/compare/v1.28.0...v1.29.0) (2022-10-26)


### Bug Fixes

* upgrade version of aws credentials to [@v1-node16](https://github.com/v1-node16) ([f623a74](https://github.com/QueroDelivery/ci/commit/f623a745f8406ee6660e37e52f9cbfa407c3fb50))


### Features

* change action to create PR deploy prod ([626d0af](https://github.com/QueroDelivery/ci/commit/626d0afa9e4ca6637f94b71a9c6f270d848c0e80))

# [1.28.0](https://github.com/QueroDelivery/ci/compare/v1.27.0...v1.28.0) (2022-10-26)


### Features

* upgrade setup node version ([21fa3cd](https://github.com/QueroDelivery/ci/commit/21fa3cd4722480fd76d3a6c569e25a49657e75f6))

# [1.27.0](https://github.com/QueroDelivery/ci/compare/v1.26.0...v1.27.0) (2022-10-26)


### Features

* change ::set-output because it was deprecated ([deab735](https://github.com/QueroDelivery/ci/commit/deab735ca15c8fcfe64d32d684edd59471fa8063))

# [1.26.0](https://github.com/QueroDelivery/ci/compare/v1.25.0...v1.26.0) (2022-09-23)


### Features

* add create ecr with initial commit ([8fc1ca2](https://github.com/QueroDelivery/ci/commit/8fc1ca2024fed262cc86ac03c9353a3688450691))

# [1.25.0](https://github.com/QueroDelivery/ci/compare/v1.24.0...v1.25.0) (2022-08-12)


### Features

* add step to creates a ecr repo ([c656b8c](https://github.com/QueroDelivery/ci/commit/c656b8cde444aebe6845ce7cf817d976ecc0e3e3))

# [1.24.0](https://github.com/QueroDelivery/ci/compare/v1.23.3...v1.24.0) (2022-08-12)


### Bug Fixes

* add ecr policy ([ab96e43](https://github.com/QueroDelivery/ci/commit/ab96e435ecab006e6409696505a1076133502c47))
* generate json in execution ([3875657](https://github.com/QueroDelivery/ci/commit/3875657fe80a7392bd5e54593eb7845a797d2927))
* generate policy in execution ([e765fee](https://github.com/QueroDelivery/ci/commit/e765feebfb399ec0ba37102c99da09e293e9c500))
* path file ([0702f0b](https://github.com/QueroDelivery/ci/commit/0702f0b4d763b6e58ceb487c753a27f2a141d153))


### Features

* add check initial commit to create ECR repositories ([e2d0c3f](https://github.com/QueroDelivery/ci/commit/e2d0c3f84390d9841a7ec89075f737ef2c3996e4))
* add step to creates a ecr repo ([8279bef](https://github.com/QueroDelivery/ci/commit/8279bef7fa4d3b3c4f16c1de8f52cf8c857dd899))

## [1.23.3](https://github.com/QueroDelivery/ci/compare/v1.23.2...v1.23.3) (2022-08-02)


### Bug Fixes

* pr close action ([19b4bb6](https://github.com/QueroDelivery/ci/commit/19b4bb67c6d2afe33037be028fe2a977b8cb6b60))

## [1.23.2](https://github.com/QueroDelivery/ci/compare/v1.23.1...v1.23.2) (2022-07-20)


### Bug Fixes

* removing debugs on k8 CI ([4fe24ad](https://github.com/QueroDelivery/ci/commit/4fe24add30194a83887b0e90c5845a7c83c2bedf))

## [1.23.1](https://github.com/QueroDelivery/ci/compare/v1.23.0...v1.23.1) (2022-07-20)


### Bug Fixes

* fixed version of kubectl on undeploy ([187f542](https://github.com/QueroDelivery/ci/commit/187f5427933934515bd17d1aa71de443df3e19f4))

# [1.23.0](https://github.com/QueroDelivery/ci/compare/v1.22.0...v1.23.0) (2022-07-19)


### Features

* Changing KUBECONFIG debug ([73c2178](https://github.com/QueroDelivery/ci/commit/73c2178b5705915c8083ccb6801fa2da0113e714))

# [1.22.0](https://github.com/QueroDelivery/ci/compare/v1.21.0...v1.22.0) (2022-07-19)


### Features

* Setting KUBECONFIG env ([1ef822e](https://github.com/QueroDelivery/ci/commit/1ef822e96de2838423e87360cea8a714911da29a))

# [1.21.0](https://github.com/QueroDelivery/ci/compare/v1.20.0...v1.21.0) (2022-07-19)


### Features

* Adding debug KUBECONFIG ([dcda669](https://github.com/QueroDelivery/ci/commit/dcda66967c8491ad48ca21a994bea7f190b0bd8e))

# [1.20.0](https://github.com/QueroDelivery/ci/compare/v1.19.2...v1.20.0) (2022-07-19)


### Features

* Adding debug .kube ([bcbd213](https://github.com/QueroDelivery/ci/commit/bcbd21344539ef83f0baaffc211ca9d5c124b16a))

## [1.19.2](https://github.com/QueroDelivery/ci/compare/v1.19.1...v1.19.2) (2022-07-10)


### Bug Fixes

* add override annotate to visibility ([91bd8d1](https://github.com/QueroDelivery/ci/commit/91bd8d1fa5e2824ebfec6c357c32e2e485f23a9f))

## [1.19.1](https://github.com/QueroDelivery/ci/compare/v1.19.0...v1.19.1) (2022-07-10)


### Bug Fixes

* set thee path ([08761b1](https://github.com/QueroDelivery/ci/commit/08761b1cf47d9b76ccdb95f4b19dab86e3cb0f51))

# [1.19.0](https://github.com/QueroDelivery/ci/compare/v1.18.0...v1.19.0) (2022-07-09)


### Features

* add visibility aand fix kubectl config ([fad1cf5](https://github.com/QueroDelivery/ci/commit/fad1cf5a5ccbae78745e14f4447e1c8667cbfb2f))

# [1.18.0](https://github.com/QueroDelivery/ci/compare/v1.17.2...v1.18.0) (2022-07-06)


### Features

* add visibility step ([73b223c](https://github.com/QueroDelivery/ci/commit/73b223c425db1cccfbebdb9b56034015f7442e8e))

## [1.17.2](https://github.com/QueroDelivery/ci/compare/v1.17.1...v1.17.2) (2022-05-05)


### Bug Fixes

* order on export path ([3d3c7d1](https://github.com/QueroDelivery/ci/commit/3d3c7d1c6c7595154a2a2a3c77d477f91230f2a0))

## [1.17.1](https://github.com/QueroDelivery/ci/compare/v1.17.0...v1.17.1) (2022-05-05)


### Bug Fixes

* install kubectl version that we downloaded ([25a9c7a](https://github.com/QueroDelivery/ci/commit/25a9c7a96c5987f4e3bae7083aff5184c6631583))

# [1.17.0](https://github.com/QueroDelivery/ci/compare/v1.16.0...v1.17.0) (2022-05-05)


### Features

* set kubectl version 1.21.0 ([853a4d6](https://github.com/QueroDelivery/ci/commit/853a4d65324cabfd397a48700260ca8342d96630))

# [1.16.0](https://github.com/QueroDelivery/ci/compare/v1.15.0...v1.16.0) (2022-05-05)


### Features

* set kubectl version to v1.22.9 ([6b86913](https://github.com/QueroDelivery/ci/commit/6b8691355679cff9507b545da7dadc086e0cd726))

# [1.15.0](https://github.com/QueroDelivery/ci/compare/v1.14.0...v1.15.0) (2022-05-05)


### Features

* set kubectl version to v1.23.6 ([e296918](https://github.com/QueroDelivery/ci/commit/e2969184b129cadae8f039ed03a94848b91b39c0))

# [1.14.0](https://github.com/QueroDelivery/ci/compare/v1.13.0...v1.14.0) (2022-05-05)


### Features

* set version on kubectl ([5482df1](https://github.com/QueroDelivery/ci/commit/5482df1729a76212790fd4942802f034c4b3bf94))

# [1.13.0](https://github.com/QueroDelivery/ci/compare/v1.12.0...v1.13.0) (2022-05-05)


### Features

* update version to kube ([ddf4b61](https://github.com/QueroDelivery/ci/commit/ddf4b6196b8c8f7b9762f84001f9f69c82ba268f))

# [1.12.0](https://github.com/QueroDelivery/ci/compare/v1.11.0...v1.12.0) (2022-05-04)


### Features

* add a specific version on kube project checkout ([eb0b721](https://github.com/QueroDelivery/ci/commit/eb0b721258675d63bf6d31fb1faa9a4c37f7e7de))

# [1.11.0](https://github.com/QueroDelivery/ci/compare/v1.10.0...v1.11.0) (2022-05-04)


### Bug Fixes

* add the right ssm-path param ([b22ddb1](https://github.com/QueroDelivery/ci/commit/b22ddb18b15fe46e9986fd4ea4f6a18a073060f6))
* empty commit ([1c485e0](https://github.com/QueroDelivery/ci/commit/1c485e0012db0e22ade7ae84ebda00602ba13339))


### Features

* add configmap file ([21a545d](https://github.com/QueroDelivery/ci/commit/21a545d201fdfa81662713ff1946c9b10ea39ddc))
* add configmap file as .kube/secrets.WF_KUBE_NAME-env-cm.yaml ([2ee3acf](https://github.com/QueroDelivery/ci/commit/2ee3acfa60d8fd9b5d3edc900307746a5175f0d2))
* add configmap reference and test step ([b27b7f9](https://github.com/QueroDelivery/ci/commit/b27b7f9b18b179f6fb31fa7bf3724795109521de))
* add empty prefix ([36c10c1](https://github.com/QueroDelivery/ci/commit/36c10c1da3f50758ae5a2759860e8a0410b06b1d))
* add kubectl apply configmap before the deployment ([432d746](https://github.com/QueroDelivery/ci/commit/432d746d1c0c28de734a6c0fa069df47d2815ac9))
* add prefix on yaml ([036a86c](https://github.com/QueroDelivery/ci/commit/036a86c74287e8ac88677d34381a63050c91855d))
* add prefix XXX ([199d4e2](https://github.com/QueroDelivery/ci/commit/199d4e23dfa7e0a248b2ad3f5008070d280838ba))
* add yaml formater ([3852915](https://github.com/QueroDelivery/ci/commit/385291548b29c69454a63c65affb226a49530ebb))
* add yaml formater 2 ([507a179](https://github.com/QueroDelivery/ci/commit/507a1796b817ae2b4690a18472c316923536778e))
* change library action-env-from-aws-ssm ([eb97ce3](https://github.com/QueroDelivery/ci/commit/eb97ce31eaab00d760a4e300e82b8b4f5f3063f0))
* change the formatter to configmap ([870623e](https://github.com/QueroDelivery/ci/commit/870623e476622b5cfadb6086dfbe8ba539b7a1a0))
* returning to properties ([fc6a990](https://github.com/QueroDelivery/ci/commit/fc6a990ce705fc6da304b4b56a4c1ba6977a0d72))
* setting kube and actionlib to main and removing logs ([ed3d1dd](https://github.com/QueroDelivery/ci/commit/ed3d1dd156c5137576480bab504063bc2846ea91))
* test ([627672e](https://github.com/QueroDelivery/ci/commit/627672ea142df5b72fccdba7271923e54acff448))
* testing changing to yaml format ([c337089](https://github.com/QueroDelivery/ci/commit/c3370891f56c461b38a2ff13c0488cc1dfd8f143))

# [1.10.0](https://github.com/QueroDelivery/ci/compare/v1.9.2...v1.10.0) (2022-03-29)


### Features

* add public host to k8s ([ef97d3e](https://github.com/QueroDelivery/ci/commit/ef97d3e350008afab88bf2bb78167fc774eb3e63))

## [1.9.2](https://github.com/QueroDelivery/ci/compare/v1.9.1...v1.9.2) (2022-03-25)


### Bug Fixes

* fix override kubefiles ([68afc07](https://github.com/QueroDelivery/ci/commit/68afc077b177841e20bbce5f5483837ecd47fafb))

## [1.9.1](https://github.com/QueroDelivery/ci/compare/v1.9.0...v1.9.1) (2022-03-25)


### Bug Fixes

* override kube files ([8338598](https://github.com/QueroDelivery/ci/commit/833859881de20be894d835b627893414461346fa))

# [1.9.0](https://github.com/QueroDelivery/ci/compare/v1.8.0...v1.9.0) (2022-03-25)


### Features

* add override kubefiles on undeploy steps and change the ci name ([eb316e0](https://github.com/QueroDelivery/ci/commit/eb316e004150c091f11b2a85672ce014bbed7730))

# [1.8.0](https://github.com/QueroDelivery/ci/compare/v1.7.4...v1.8.0) (2022-03-25)


### Features

* add override kubefiles - OK ([138ae4c](https://github.com/QueroDelivery/ci/commit/138ae4ca49a96e60ea86b5e2c40c974fa5cecf33))

## [1.7.4](https://github.com/QueroDelivery/ci/compare/v1.7.3...v1.7.4) (2022-03-25)


### Bug Fixes

* try copy *.yml in directory ([c0c701f](https://github.com/QueroDelivery/ci/commit/c0c701ffcbf6631b33e818f2de5aff301589493a))

## [1.7.3](https://github.com/QueroDelivery/ci/compare/v1.7.2...v1.7.3) (2022-03-25)


### Bug Fixes

* testing copying files ([461f64f](https://github.com/QueroDelivery/ci/commit/461f64f3d7a02ecd5662794234b9eb11733b0b33))

## [1.7.2](https://github.com/QueroDelivery/ci/compare/v1.7.1...v1.7.2) (2022-03-25)


### Bug Fixes

* testing file exist in Override kubefiles steps ([8ad5808](https://github.com/QueroDelivery/ci/commit/8ad580813f4f7730cc35d9fcf1cf15cb753bfbf4))

## [1.7.1](https://github.com/QueroDelivery/ci/compare/v1.7.0...v1.7.1) (2022-03-25)


### Bug Fixes

* add comments on step Override kubefiles ([4caed18](https://github.com/QueroDelivery/ci/commit/4caed1834b08246b35867b4ad4388b9bce3c8ac6))

# [1.7.0](https://github.com/QueroDelivery/ci/compare/v1.6.0...v1.7.0) (2022-03-25)


### Features

* add copy files in Override kubefiles ([42e2c36](https://github.com/QueroDelivery/ci/commit/42e2c36c20999a0948ff7ce7c049a991f14b1c7d))

# [1.6.0](https://github.com/QueroDelivery/ci/compare/v1.5.0...v1.6.0) (2022-03-25)


### Features

* add Override kubefiles 2 ([b7f0442](https://github.com/QueroDelivery/ci/commit/b7f0442c15c722d1dba4e50b613c5ff817ba4d26))

# [1.5.0](https://github.com/QueroDelivery/ci/compare/v1.4.0...v1.5.0) (2022-03-25)


### Features

* add Override kubefiles step ([a342341](https://github.com/QueroDelivery/ci/commit/a34234161da47848148474fd4f2958a39ea786f2))

# [1.4.0](https://github.com/QueroDelivery/ci/compare/v1.3.1...v1.4.0) (2022-03-25)


### Features

* add override kubefiles ([7e75678](https://github.com/QueroDelivery/ci/commit/7e756788ae4bc2cb9cebffab97bff6593dee773e))

## [1.3.1](https://github.com/QueroDelivery/ci/compare/v1.3.0...v1.3.1) (2022-03-14)


### Bug Fixes

* add persist-credentials false to work with protected branches ([1adad4d](https://github.com/QueroDelivery/ci/commit/1adad4d6d4ddf019c443607c0f4d20a04a339e9d))

# [1.3.0](https://github.com/QueroDelivery/ci/compare/v1.2.0...v1.3.0) (2022-03-08)


### Features

* add the checkout with attribute ref: main ([1059f22](https://github.com/QueroDelivery/ci/commit/1059f229e10ba95449e961aa66111fe9c514c918))

# [1.2.0](https://github.com/QueroDelivery/ci/compare/v1.1.7...v1.2.0) (2022-03-08)


### Features

* add right k8 configuration ([f5f4463](https://github.com/QueroDelivery/ci/commit/f5f4463254ddd034e885cfaaaed67798209e3d2b))

## [1.1.7](https://github.com/QueroDelivery/ci/compare/v1.1.6...v1.1.7) (2022-03-08)


### Bug Fixes

* cat namespace.yml to test4 ([e0503c2](https://github.com/QueroDelivery/ci/commit/e0503c2ed76ae8499408570dbcc5c2e47ff5e062))

## [1.1.6](https://github.com/QueroDelivery/ci/compare/v1.1.5...v1.1.6) (2022-03-08)


### Bug Fixes

* cat namespace.yml to test3 ([42abbf6](https://github.com/QueroDelivery/ci/commit/42abbf603ff834da5c21bc17435e9f9b63075f8f))

## [1.1.5](https://github.com/QueroDelivery/ci/compare/v1.1.4...v1.1.5) (2022-03-08)


### Bug Fixes

* cat namespace.yml to test2 ([922c955](https://github.com/QueroDelivery/ci/commit/922c955b859adefcc85dcb961fe05ac6d92f87d0))

## [1.1.4](https://github.com/QueroDelivery/ci/compare/v1.1.3...v1.1.4) (2022-03-08)


### Bug Fixes

* cat namespace.yml to test ([50ee360](https://github.com/QueroDelivery/ci/commit/50ee360fd5915db40caf1bf16621e29238ab0ac5))

## [1.1.3](https://github.com/QueroDelivery/ci/compare/v1.1.2...v1.1.3) (2022-03-08)


### Bug Fixes

* setting the PR_NUMBER and SERVICE_NAME ([62b2386](https://github.com/QueroDelivery/ci/commit/62b23861b7e6ccdf09c18a5d08e9a2e54ed9829e))

## [1.1.2](https://github.com/QueroDelivery/ci/compare/v1.1.1...v1.1.2) (2022-03-08)


### Bug Fixes

* setting the PR_NUMBER ([73ecfec](https://github.com/QueroDelivery/ci/commit/73ecfec73855155a981b553bcd43734f8d4865ff))

## [1.1.1](https://github.com/QueroDelivery/ci/compare/v1.1.0...v1.1.1) (2022-03-08)


### Bug Fixes

* add WF_KUBE_TYPE in the undeploy step ([4ac9633](https://github.com/QueroDelivery/ci/commit/4ac96331cac9dec9b56dd3dda7c05cc6614aafd3))

# [1.1.0](https://github.com/QueroDelivery/ci/compare/v1.0.1...v1.1.0) (2022-03-07)


### Features

* add doc example ([0f169e6](https://github.com/QueroDelivery/ci/commit/0f169e6f30dbde3a72cc3dcaf0b77875241b0c8d))

## [1.0.1](https://github.com/QueroDelivery/ci/compare/v1.0.0...v1.0.1) (2022-03-07)


### Bug Fixes

* return the ci files to the top level directory .workflow ([405d258](https://github.com/QueroDelivery/ci/commit/405d2584076c5020c27f50de532741f6e250589c))

# 1.0.0 (2022-03-07)


### Bug Fixes

* add aws credentials ([88fa72a](https://github.com/QueroDelivery/ci/commit/88fa72ab88a336323e6e4a7205e7bf9cecca3ebc))
* add inputs ([f020fd3](https://github.com/QueroDelivery/ci/commit/f020fd3c06cf6a66c08e2f392960bcf3085c5df2))
* add KUBE_NAME as env on step k8 deploy ([a0b2ae4](https://github.com/QueroDelivery/ci/commit/a0b2ae4663db28d0d189cc3580f90e43033b34eb))
* add output-registry ([0a0bd59](https://github.com/QueroDelivery/ci/commit/0a0bd593b95ab4636c71bda2f26894984b0f58cb))
* add WF_SERVICE_NAME as required ([95d07ad](https://github.com/QueroDelivery/ci/commit/95d07ad74a1fcc2770a78178d6b8f830d4ae2ec2))
* aws credentials service name ([531c654](https://github.com/QueroDelivery/ci/commit/531c65476ba381384713093388fbba0011655d92))
* aws role secrets ([158bc2c](https://github.com/QueroDelivery/ci/commit/158bc2c7017f5dc93a0abdd5d72acb92b0f8ccab))
* fixes the step confiigurations ([0b88d3d](https://github.com/QueroDelivery/ci/commit/0b88d3d5fe5db107b418c678b4b5edd26c19a337))
* mapping outputs ([aeaa60b](https://github.com/QueroDelivery/ci/commit/aeaa60bb91aaa940fff37cc1ebfea9083fae1a9a))
* removing env_type ([8daf3fb](https://github.com/QueroDelivery/ci/commit/8daf3fb33dc3564a77bf0ebb1c4d981b12c75a49))
* removing environment ([569fb64](https://github.com/QueroDelivery/ci/commit/569fb6426117255553e42ee3b0daa7718477bc51))
* removing kubedomain as required variable ([cf23b61](https://github.com/QueroDelivery/ci/commit/cf23b6143bf6fc6446af336b30d19b78c9ee7aef))
* removing print ([f5dd839](https://github.com/QueroDelivery/ci/commit/f5dd8399d5813c4977cb8be58d418b3674e879af))
* removing role to assume on aws credentials ([80a6c44](https://github.com/QueroDelivery/ci/commit/80a6c4476051825130cbed146d6c2c67e7af386e))
* removing role-session-name ([9533a8d](https://github.com/QueroDelivery/ci/commit/9533a8d3c1ec64514f59ae8fda2966e57ebcc741))
* removing unnecessaries variables ([3cf5674](https://github.com/QueroDelivery/ci/commit/3cf567447689e9c979a6c366caed1ade841f161b))
* removing WF_ECR_REGISTRY ([db5b69d](https://github.com/QueroDelivery/ci/commit/db5b69d97357bdc4c3ebdc8f6f9feaa57ef0beaf))
* removing WF_NEW_CI variable ([7d3c3ca](https://github.com/QueroDelivery/ci/commit/7d3c3cab817afd9a926dd9f1b7f10e63321cfcdd))
* rename CI ([e23405f](https://github.com/QueroDelivery/ci/commit/e23405fcdb4f6fa9d1794b8e247e7b8b745a6a22))
* servicename output ([485d24d](https://github.com/QueroDelivery/ci/commit/485d24d4bf0139e77bc562485caa673507e1ff74))


### Features

* add - run: git checkout HEAD^ ([e62955a](https://github.com/QueroDelivery/ci/commit/e62955af1b4b63b699203cc5be8e5532098aac1f))
* add ${{ env.GIT_HEAD_HASH }} ([5343839](https://github.com/QueroDelivery/ci/commit/5343839b473356e1be2841f79650214f54eae84b))
* add a step Update code with new version ([e87796f](https://github.com/QueroDelivery/ci/commit/e87796fa981a20f437b48c2db846933b4b637c77))
* add a step Update code with new version 2 ([447f27d](https://github.com/QueroDelivery/ci/commit/447f27db8da98379696b131739fa93df2330a8ed))
* add a step Update code with new version 3 ([0f6911f](https://github.com/QueroDelivery/ci/commit/0f6911f7e8f0aff501912fb9ec6db99af13daaac))
* add aws credentials ([e357712](https://github.com/QueroDelivery/ci/commit/e357712b661e46f2d21a95421878966340cc4d64))
* add aws credentials step ([9c72288](https://github.com/QueroDelivery/ci/commit/9c72288024a4d9698fe1f4d08669d675ce1ea4da))
* add checkout and removing fetch depth 0 ([f1a0e81](https://github.com/QueroDelivery/ci/commit/f1a0e81cf32d50135265704c61c32539639b3616))
* add ci-k8-base.yml ([821dc6e](https://github.com/QueroDelivery/ci/commit/821dc6ebdc4f7ee9dd2cf8370b438361a1fe4414))
* add conditional on ecr login ([d1798a0](https://github.com/QueroDelivery/ci/commit/d1798a03744e2aed96e84738a776f9df8ff0c26c))
* add conditional prod and stage env ([f76cfe9](https://github.com/QueroDelivery/ci/commit/f76cfe9b0422b34f9449797c3e7b9b2ac78008ae))
* add create pr to prod ([f8ad296](https://github.com/QueroDelivery/ci/commit/f8ad296ca94daa46e5327564898c0dac4638e7d5))
* add echo version tag ([15fafae](https://github.com/QueroDelivery/ci/commit/15fafae456c78c128ef104422b17bfa89b1047eb))
* add ecr workflow ([df90127](https://github.com/QueroDelivery/ci/commit/df901274ff62d4bbe406fafa89c5847438bd6f6b))
* add ecrregistry output ([e2104ff](https://github.com/QueroDelivery/ci/commit/e2104ff916a7ec389b700267c84a287bd23407c3))
* add envs ([f7f8892](https://github.com/QueroDelivery/ci/commit/f7f8892ce01e7bbec5bd08beb64365259454b613))
* add external private action ([93adfb3](https://github.com/QueroDelivery/ci/commit/93adfb32f59434e8da58871e0c09b60a4e5a58d3))
* add external private action ([a849167](https://github.com/QueroDelivery/ci/commit/a8491679ab4708e19db0bab2926360db5b359eec))
* add external private action 2 ([67eb7f3](https://github.com/QueroDelivery/ci/commit/67eb7f3526196ddc6d6705fbf69de122c86473bc))
* add external private action 3 ([b98c213](https://github.com/QueroDelivery/ci/commit/b98c21312c4e277a3d6dceda1287c4c67d18b1aa))
* add external private action 4 ([595ca38](https://github.com/QueroDelivery/ci/commit/595ca38a2ae750ee2aab3126509ce01956ad57cc))
* add external private action 5 ([867f4b6](https://github.com/QueroDelivery/ci/commit/867f4b6ace45404f32c06f7557159bbc9c60aa6c))
* add getting current branch ([3906946](https://github.com/QueroDelivery/ci/commit/3906946852ff6f17cf83a9baba4735d874c4ea17))
* add getting the last hash ([b2f68d7](https://github.com/QueroDelivery/ci/commit/b2f68d7a3d2021385d3f3fb2725f9d2de8850844))
* add github token ([39eae30](https://github.com/QueroDelivery/ci/commit/39eae30dd91feec600e9cb9ba04bc8cb345b34ce))
* add github_token ans input ([777e3e7](https://github.com/QueroDelivery/ci/commit/777e3e79d8b9035241055dcc19211aaf1ac5f7ba))
* add input and secrets ([2cd39e0](https://github.com/QueroDelivery/ci/commit/2cd39e02e6c29bdf361e96614e144ba9a7f1420f))
* add inputs ([2d8b795](https://github.com/QueroDelivery/ci/commit/2d8b79556c971fc126f15e2f7a851580c449dc51))
* add inputs ([c2ceb16](https://github.com/QueroDelivery/ci/commit/c2ceb165a806682040a53de518af424b08a004dd))
* add kube environments as secrets ([03029f8](https://github.com/QueroDelivery/ci/commit/03029f8ee2ea73993bdb5ce48974be24a5012140))
* add kube files and removing unnecessaries steps ([f0edf3a](https://github.com/QueroDelivery/ci/commit/f0edf3a15095ae03f516589585cb1626517210c1))
* add listing directory and path ([26593e2](https://github.com/QueroDelivery/ci/commit/26593e2b6f5505e5be9a6240d38e41e0aa4b3913))
* add listing directory and path 2 ([e9b33ba](https://github.com/QueroDelivery/ci/commit/e9b33badacb0ef2866a27e0f38e53dc9f7726ee1))
* add login on aws ecr ([d5d344f](https://github.com/QueroDelivery/ci/commit/d5d344f517b004b3c782217e19e91c34be53ffbb))
* add mapping output ([2cbc3ff](https://github.com/QueroDelivery/ci/commit/2cbc3ff79643a1dc2e923f649235a1ddb4830c1c))
* add nodeversion as parameter ([e8b4228](https://github.com/QueroDelivery/ci/commit/e8b42289b98db2912427e3084c29758b5faafaa4))
* add nodeversion as parameter and reoving node strategy ([fc69cc9](https://github.com/QueroDelivery/ci/commit/fc69cc9dfe19283a1063c3599a4db6804cc8c03f))
* add outputs servicename, image, ecrregistry ([c586820](https://github.com/QueroDelivery/ci/commit/c5868204cc9d7772f7e5121af797a175b8f979fe))
* add parameter store step ([3830223](https://github.com/QueroDelivery/ci/commit/3830223c0552c0188fcc5b329f9f981a5af825a2))
* add print ect ([5842039](https://github.com/QueroDelivery/ci/commit/58420397fa5f87779a1bff5af2f52f1bddac76fa))
* add registry as secrets and change test:ci ([fe066f1](https://github.com/QueroDelivery/ci/commit/fe066f1d2d6427cef54c6a7ac5dc2f959db2931c))
* add release step ([44a406b](https://github.com/QueroDelivery/ci/commit/44a406b95da922bbafa69d4bc3ddfe92dbda2a3f))
* add role as secrets ([9d79b07](https://github.com/QueroDelivery/ci/commit/9d79b07c73bddf34e86495a0e0c9b14759b3f5ba))
* add roles variables ([250e3bc](https://github.com/QueroDelivery/ci/commit/250e3bc75d1da9307d79369fedd8048a4b76cbab))
* add semantic-release ([c520c57](https://github.com/QueroDelivery/ci/commit/c520c577ac08cbe25b39c4746a92519971461e8f))
* add semantic-release and gitignore ([d922a7f](https://github.com/QueroDelivery/ci/commit/d922a7fcc6383822aef4fb1ce10fdfec5586e4bf))
* add semantic-release and gitignore ([12069c1](https://github.com/QueroDelivery/ci/commit/12069c128e905b3ac526fe263a90753981c88cd1))
* add semantic-release and gitignore ([b051aef](https://github.com/QueroDelivery/ci/commit/b051aef529a8af99fab9a5c0971011ffe776adf8))
* add servicename ([802375c](https://github.com/QueroDelivery/ci/commit/802375ca7da83c276fd017501936c8b5799063cb))
* add the step getting commit hash ([f5783db](https://github.com/QueroDelivery/ci/commit/f5783db0cc13b91869d4f5a05a80222de2540ea9))
* add undeploy feature ([e9a3a26](https://github.com/QueroDelivery/ci/commit/e9a3a26b9080b6575877907ad92bb1cf09f44277))
* add undeploy workflow ([5a63018](https://github.com/QueroDelivery/ci/commit/5a6301893130dc0b147e645028e6e7520b6523e8))
* add undeploy workflow with servicename ([b5e0c40](https://github.com/QueroDelivery/ci/commit/b5e0c40445daf8a3bc48cb35adb4b9777e92470d))
* add WF_GITHUB_TOKEN to be used on checkout steps ([7c64a8e](https://github.com/QueroDelivery/ci/commit/7c64a8e92bf11b02eb4dcc45ec3f12a3f45a6197))
* add WF_KUBE_DEPLOYMENT ([19ee356](https://github.com/QueroDelivery/ci/commit/19ee35683f7c1a4eff40bfdbf77851b4af4e4092))
* adding cache and checkout ([1cdf066](https://github.com/QueroDelivery/ci/commit/1cdf0663f3f0c1104e22ccc2fa49b002ff223a81))
* adding test ([e7c5bd1](https://github.com/QueroDelivery/ci/commit/e7c5bd1fd2a60630d404ecc3dcd0b1a47510d040))
* change kube secrepts to default input string ([ff522f5](https://github.com/QueroDelivery/ci/commit/ff522f56dd6f0ab2e92576048e4d2e91d9995712))
* change variable names ([d1eb0c1](https://github.com/QueroDelivery/ci/commit/d1eb0c13eead398570f8128f920b2466276e6da4))
* changing the version checkout to v3 ([748c06e](https://github.com/QueroDelivery/ci/commit/748c06e7f057313d01b8c03879f0c932656c833f))
* create the release actions structure ([d530a19](https://github.com/QueroDelivery/ci/commit/d530a195f8bf31ca098be8a098f124c391457ebb))
* creating a comment as parameter ([73d7830](https://github.com/QueroDelivery/ci/commit/73d783070e623888e8aea5b6871f5d737eb32b9e))
* creating a comment as parameter required false ([34c53bb](https://github.com/QueroDelivery/ci/commit/34c53bb141805d3b8fb33dda97fd5a372dc9993f))
* creating the base node build ci ([27dbeb0](https://github.com/QueroDelivery/ci/commit/27dbeb0649b539d1f15d258d4d2075c6a655fc28))
* getting registry from login-ecr step ([4dc786e](https://github.com/QueroDelivery/ci/commit/4dc786ee436ac2892e91e4f2d5a2ce0c675620c2))
* new base_node_build with cache and setup node ([3c46770](https://github.com/QueroDelivery/ci/commit/3c46770bf409c352fe74ab99e9d314c02800b903))
* remove user input ([d3afaa7](https://github.com/QueroDelivery/ci/commit/d3afaa763ad149f17c447ccfe0bb14691395d96f))
* removing cachewq ([0d31f93](https://github.com/QueroDelivery/ci/commit/0d31f9389357022aec59375bd0aee4cfb15c921a))
* removing on push ([119e2bc](https://github.com/QueroDelivery/ci/commit/119e2bc97e4996b4ec3299728d915ac6222de561))
* removing output WF_ECR_REGISTRY and image ([7e0fdbd](https://github.com/QueroDelivery/ci/commit/7e0fdbdf3aa9a3c8029486ec17698fbbfad2c6a7))
* removing test ([f981fde](https://github.com/QueroDelivery/ci/commit/f981fde271fd8ac28529e661a6967e9244185a39))
* removinng gettext ([4ef667d](https://github.com/QueroDelivery/ci/commit/4ef667da4632345fd2c393f7b3109df1c4774956))
* rename ([4b4b0da](https://github.com/QueroDelivery/ci/commit/4b4b0da296ca025a7246119105a1be61a214aee4))
* renaming cik8 ([8398c19](https://github.com/QueroDelivery/ci/commit/8398c1949461820c75e93c03d993fe2c1b6c9083))
* setting release to execute only once ([47e0fcc](https://github.com/QueroDelivery/ci/commit/47e0fcc43a00cd87134f36a35ac2104417ca1da1))
* setting setting persist credentials false ([093a5ec](https://github.com/QueroDelivery/ci/commit/093a5ec47ba9a6f47db4570056ba669c400a8dd1))
* testing ecr ([3950f96](https://github.com/QueroDelivery/ci/commit/3950f96b60b54a4d8bcc8248b7f17b8bee9ae966))
* testing ecr 1 ([5b4829d](https://github.com/QueroDelivery/ci/commit/5b4829dc7b59b26ac3b15dfad7628704f31900b3))
* testing ecr 2 ([738cf9d](https://github.com/QueroDelivery/ci/commit/738cf9d3cc7c20a088f9e8911e598f80e9fc03d9))
* testing ecr 3 ([9561b3f](https://github.com/QueroDelivery/ci/commit/9561b3fd8d02a185737fbfcde3c889425820f82a))
* testing ecr 4 ([d18ed66](https://github.com/QueroDelivery/ci/commit/d18ed662d508206f1eb967c2aa965d615b30d8be))
* testing ecr 5 ([696ecdc](https://github.com/QueroDelivery/ci/commit/696ecdc1c0ff23337357e1c335b12ff4e480cea1))
* testing ecr 5 ([282e566](https://github.com/QueroDelivery/ci/commit/282e566bc588619012982ee16a669a7d0f7c6d9e))
* testing ecr 6 ([b29d2e6](https://github.com/QueroDelivery/ci/commit/b29d2e6c42912c2f94f4f7ed0b7324166b141481))
* testing ecr 7 ([f757b5b](https://github.com/QueroDelivery/ci/commit/f757b5b08a5567b75378d0820469f3f247d89b40))
* update checkout from v2 to v3 ([96c37b6](https://github.com/QueroDelivery/ci/commit/96c37b67e4dc3a2aec362533ea26a986bf61f030))
* update the cache and setup node ([70025c5](https://github.com/QueroDelivery/ci/commit/70025c56108daf27b439bb849ee3c1453e17f164))
* updating the code with the last version released ([0337075](https://github.com/QueroDelivery/ci/commit/0337075c52ec39e03aba59da2b68240ec712395c))
* upgrade the cache version ([d8b1528](https://github.com/QueroDelivery/ci/commit/d8b1528a52413848f7536e923412d96cb9e7ca23))
* WF_SHOW_COMMENT with value true 2 ([03f7ee9](https://github.com/QueroDelivery/ci/commit/03f7ee916447a39cea51b167a3aec6ffbac5fc72))
* WF_SHOW_COMMENT with value true 3 ([920fd9b](https://github.com/QueroDelivery/ci/commit/920fd9ba89352d48e8b6842d0f441215d1888f4f))
* WF_SHOW_COMMENT with value true 4 ([809123f](https://github.com/QueroDelivery/ci/commit/809123f04d2a9f82ca0e1df5e308707a66effb57))
