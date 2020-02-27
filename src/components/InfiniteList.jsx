import * as React from 'react';
import PropTypes from 'prop-types';
import Immutable from 'immutable';
import InfiniteLoader from "react-window-infinite-loader";
import { AutoSizer, List  } from 'react-virtualized';


const STATUS_LOADING = 1;
const STATUS_LOADED = 2;

export default class InfiniteLoaderExample extends React.PureComponent {
  static contextTypes = {
    list: PropTypes.instanceOf(Immutable.List).isRequired,
  };

  constructor(props) {
    super(props);

    this.state = {
      loadedRowCount: 0,
      loadedRowsMap: {},
      loadingRowCount: 0,
    };

    this._timeoutIdMap = {};

    this._clearData = this._clearData.bind(this);
    this._isRowLoaded = this._isRowLoaded.bind(this);
    this._loadMoreRows = this._loadMoreRows.bind(this);
    this._rowRenderer = this._rowRenderer.bind(this);
  }

  componentWillUnmount() {
    Object.keys(this._timeoutIdMap).forEach(timeoutId => {
      clearTimeout(timeoutId);
    });
  }

  render() {
    const {list} = this.context;

    return (
        <InfiniteLoader
        isRowLoaded={this._isRowLoaded}
        loadMoreRows={this._loadMoreRows}
        rowCount={list.size}>
        {({onRowsRendered, registerChild}) => (
          <AutoSizer disableHeight>
            {({width}) => (
              <List
                ref={registerChild}
                height={200}
                onRowsRendered={onRowsRendered}
                rowCount={list.size}
                rowHeight={30}
                rowRenderer={this._rowRenderer}
                width={width}
              />
            )}
          </AutoSizer>
        )}
      </InfiniteLoader>
    );
  }

  _clearData() {
    this.setState({
      loadedRowCount: 0,
      loadedRowsMap: {},
      loadingRowCount: 0,
    });
  }

  _isRowLoaded({index}) {
    const {loadedRowsMap} = this.state;
    return !!loadedRowsMap[index]; // STATUS_LOADING or STATUS_LOADED
  }

  _loadMoreRows({startIndex, stopIndex}) {
    const {loadedRowsMap, loadingRowCount} = this.state;
    const increment = stopIndex - startIndex + 1;

    for (var i = startIndex; i <= stopIndex; i++) {
      loadedRowsMap[i] = STATUS_LOADING;
    }

    this.setState({
      loadingRowCount: loadingRowCount + increment,
    });

    const timeoutId = setTimeout(() => {
      const {loadedRowCount, loadingRowCount} = this.state;

      delete this._timeoutIdMap[timeoutId];

      for (var i = startIndex; i <= stopIndex; i++) {
        loadedRowsMap[i] = STATUS_LOADED;
      }

      this.setState({
        loadingRowCount: loadingRowCount - increment,
        loadedRowCount: loadedRowCount + increment,
      });

      promiseResolver();
    }, 1000 + Math.round(Math.random() * 2000));

    this._timeoutIdMap[timeoutId] = true;

    let promiseResolver;

    return new Promise(resolve => {
      promiseResolver = resolve;
    });
  }

  _rowRenderer({index, key, style}) {
    const {list} = this.context;
    const {loadedRowsMap} = this.state;

    const row = list.get(index);
    let content;

    if (loadedRowsMap[index] === STATUS_LOADED) {
      content = row.name;
    } else {
      content = (
        <div  style={{width: row.size}} />
      );
    }

    return (
      <div  key={key} style={style}>
        {content}
      </div>
    );
  }
}