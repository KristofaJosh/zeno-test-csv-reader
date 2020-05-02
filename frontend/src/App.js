import React, {useEffect, useState} from 'react';
import './App.css';
import axios from 'axios';

function App() {
    const [fileUpload, setUpload] = useState({file: ''});
    const [messageStatus, setStatus] = useState({loading: false, message: ''});
    const [buttonStates, setButtonStates] = useState({loading: false, status: 'detach'});
    const [data, setData] = useState([]);

    useEffect(() => {
        setStatus({loading: true, message: 'Retrieving Data ...'});
        axios({
            method: 'GET',
            url: 'http://127.0.0.1:8000/csv_db/',
        }).then((response) => {
            setData(response.data);
            if (response.data.length > 0) {
                setStatus({loading: false, message: 'Data Updated'});
            } else {
                setStatus({loading: false, message: 'No Data'});
            }
        }).catch((err) => {
            setStatus({loading: false, message: 'Error Occurred, Try again'});
        });

    }, [buttonStates]);

    const handleChange = (e) => {
        e.preventDefault();
        setUpload({file: e.target.files[0]})
    };

    const submitForm = (e) => {
        e.preventDefault();
        if (fileUpload.file !== '') {
            setButtonStates({loading: true, status: 'detaching...'});
            setStatus({loading: true, message: 'uploading ...'});

            const formData = new FormData();
            formData.append('file', fileUpload.file);

            axios({
                method: 'PATCH',
                url: 'http://127.0.0.1:8000/upload/',
                data: formData
            }).then((response) => {
                if (response.status === 201) {
                    setButtonStates({loading: false, status: 'detached'});
                    setStatus({loading: false, message: 'Uploaded!'});
                }

            }).catch((err) => {
                setButtonStates({loading: false, status: 'detach'});
                if (err.response.status === 500) {
                    setStatus({loading: false, message: 'Invalid File format'});
                }
            });
        }
    };


    return (
        <div className={'App'}>
            <div className={'content'}>
                <div className="logo">
                    <img src="/assets/images/Zeno.jpg" alt=""/>
                    <p style={{fontWeight: 'bolder'}}>CSV TO DB SKILL ASSESSMENT</p>
                    <p>{messageStatus.message}</p>

                </div>
                <div className={'form'}>
                    <h3>Upload CSV</h3>

                    <span>
                        <input type="file" accept={'csv'} onChange={handleChange}/>
                        <button type={'submit'} onClick={submitForm} disabled={buttonStates.loading}>
                            {buttonStates.loading ? buttonStates.status : buttonStates.status}
                        </button>

                    </span>
                </div>
                <div className={'csv'}>
                    <div className={'header'}><h2>CSV Data</h2></div>
                    <span className={'csv-head'}>
                        <div className={'card-info'}>
                            <span>ID</span>
                            <span>Temperature</span>
                            <span>Duration</span>
                            <span>TimeStamp</span>
                        </div>
                    </span>


                    {data.length === 0 ?
                        <div className="csvbody">
                            <p>{buttonStates.loading ? 'Loading ...' : 'No Data Found'}</p>
                        </div>

                        :
                        data.map((el) => (
                            <div className={'card'}>
                                <div key={el.idd} className={'card-info'}>
                                    <span>{el.idd}</span>
                                    <span>{el.temperature}</span>
                                    <span>{el.duration}</span>
                                    <span>{el.timestamp}</span>
                                </div>
                                {/*<button type={'submit'} onClick={submitForm}>edit</button>*/}
                            </div>
                        ))

                    }


                </div>
            </div>
        </div>
    );
}

export default App;
