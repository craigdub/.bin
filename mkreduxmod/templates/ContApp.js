import React, { Component } from 'react';
import { connect } from 'react-redux';
import {
  StackNavigator,
} from 'react-navigation';

import App from '../components/App';

import { User } from '../../globals/models'

const mapStateToProps = (state, ownProps) => {
  return {
    fbUser: state.fbUser,
    user: state.user,
  }
};

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
  }
};

const ExploreApp = connect(
  mapStateToProps,
  mapDispatchToProps
)(App);

const ExploreAppStackNavigator = StackNavigator({
    ExploreAppStack: { screen: ExploreApp },
});
export default ExploreAppStackNavigator;
