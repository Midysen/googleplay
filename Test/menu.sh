#��ȡgoogle play�ϵ�Ӧ����Ϣ���洢�����ݿ�
#cd ./apkinfo_v1.1-CN/ 
#scrapy crawl google

if [ $? ]
then
    cd /home/openthos/AppStore/
    echo "success"
    #app��Ϣȥ��
    python DuplicateRemoval.py
    #��������apk
    node down_main_all.js
    if [ $? ]
    then
        #��������apk��ͼ��
        python download_img.py
        if [ $? ]
        then
            #�����Ѿ����ص�apk�ļ���������openthosӦ���̵���Ҫ����Ϣ
            python aapt.py
            if [ $? ]
            then
                #����Ӧ���̵���Ҫ��all�ļ���game�ļ�
                python aggregate.py
            fi
        fi
    fi
fi
#�ϴ�Ӧ���̵���Ҫ���ļ���180������
./push.sh
